from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
import os
import zipfile
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

# Configurações
PROVAS_DIR = 'provas'
RESPOSTAS_DIR = 'respostas'
UPLOAD_FOLDER = RESPOSTAS_DIR
ALLOWED_EXTENSIONS = {'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garantir que os diretórios existam
os.makedirs(PROVAS_DIR, exist_ok=True)
os.makedirs(RESPOSTAS_DIR, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prova')
def download_prova():
    prova_path = os.path.join(PROVAS_DIR, 'prova.pdf')
    if os.path.exists(prova_path):
        return send_file(prova_path, as_attachment=True)
    else:
        return "Prova não encontrada", 404

@app.route('/upload', methods=['POST'])
def upload_resposta():
    # Verificar se o aluno foi fornecido
    aluno = request.form.get('aluno', 'aluno_desconhecido')
    
    if 'resposta' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['resposta']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file and allowed_file(file.filename):
        # Gerar nome único para o arquivo
        filename = secure_filename(f"{aluno}_{uuid.uuid4().hex}.zip")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Salvar o arquivo
        file.save(filepath)
        
        return jsonify({
            'message': 'Resposta enviada com sucesso',
            'aluno': aluno,
            'arquivo': filename
        })
    else:
        return jsonify({'error': 'Tipo de arquivo não permitido. Use apenas arquivos ZIP.'}), 400

if __name__ == '__main__':
    # Iniciar o servidor na interface de loopback e porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)