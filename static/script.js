document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const statusDiv = document.getElementById('status');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                statusDiv.textContent = data.message;
                statusDiv.className = 'success';
                form.reset();
            } else if (data.error) {
                statusDiv.textContent = data.error;
                statusDiv.className = 'error';
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            statusDiv.textContent = 'Erro ao enviar o arquivo. Tente novamente.';
            statusDiv.className = 'error';
        });
    });
});