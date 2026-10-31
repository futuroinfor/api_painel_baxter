  function updateTime() {
    const timeElement = document.getElementById('current-time');
    const now = new Date();
    
    // Formata a hora no padrão de 24 horas (HH:MM:SS) com dois dígitos
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    timeElement.textContent = `${hours}:${minutes}:${seconds}`;
  }

  // Executa a função imediatamente para não esperar o primeiro segundo passar
  updateTime();
  
  // Atualiza o relógio a cada 1000 milissegundos (1 segundo)
  setInterval(updateTime, 1000);