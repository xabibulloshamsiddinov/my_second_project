<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Habibullo | Web Sahifa</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: black;
      color: #00ffff;
      font-family: "Courier New", monospace;
      overflow: hidden;
    }
    canvas {
      position: fixed;
      top: 0;
      left: 0;
      z-index: 0;
    }
    .container {
      position: relative;
      z-index: 2;
      text-align: center;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(0, 0, 50, 0.7);
      padding: 50px;
      border-radius: 20px;
      box-shadow: 0 0 30px #00ffff, inset 0 0 20px rgba(0, 255, 255, 0.2);
      width: 85%;
      max-width: 800px;
      margin: auto;
      animation: glow-pulse 3s ease-in-out infinite;
    }
    
    @keyframes glow-pulse {
      0%, 100% {
        box-shadow: 0 0 30px #00ffff, inset 0 0 20px rgba(0, 255, 255, 0.2);
      }
      50% {
        box-shadow: 0 0 50px #00ffff, inset 0 0 30px rgba(0, 255, 255, 0.4);
      }
    }
    
    h1 {
      font-size: 2.5em;
      text-shadow: 0 0 10px #00ffff;
      margin: 0 0 20px 0;
      letter-spacing: 2px;
      animation: type-in 2s ease-out;
    }
    
    @keyframes type-in {
      from {
        opacity: 0;
        text-shadow: 0 0 0 #00ffff;
      }
      to {
        opacity: 1;
        text-shadow: 0 0 10px #00ffff;
      }
    }
    
    .subtitle {
      font-size: 1.3em;
      color: #00ff88;
      margin: 15px 0;
      animation: fade-in 1.5s ease-out 0.5s both;
    }
    
    .contact-section {
      margin-top: 30px;
      padding-top: 30px;
      border-top: 2px dashed #00ffff;
      animation: fade-in 1.5s ease-out 1s both;
    }
    
    .contact-title {
      font-size: 1.2em;
      margin-bottom: 15px;
      color: #00ffff;
      text-transform: uppercase;
      letter-spacing: 3px;
    }
    
    p {
      font-size: 1.1em;
      margin: 10px 0;
      animation: fade-in 1.5s ease-out 1.5s both;
    }
    
    a {
      color: #00ff88;
      text-decoration: none;
      font-weight: bold;
      transition: all 0.3s ease;
      padding: 5px 10px;
      border-radius: 5px;
    }
    
    a:hover {
      color: #00ffff;
      text-shadow: 0 0 15px #00ffff;
      background: rgba(0, 255, 136, 0.1);
      transform: scale(1.1);
    }
    
    .btn {
      display: inline-block;
      margin-top: 25px;
      padding: 15px 35px;
      border: 2px solid #00ffff;
      border-radius: 10px;
      transition: all 0.3s ease;
      font-size: 1.1em;
      font-weight: bold;
      cursor: pointer;
      animation: fade-in 1.5s ease-out 2s both;
      background: rgba(0, 255, 255, 0.1);
    }
    
    .btn:hover {
      background: #00ffff;
      color: black;
      box-shadow: 0 0 20px #00ffff;
      transform: scale(1.05);
    }
    
    .profile-info {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 25px;
      padding: 20px;
      background: rgba(0, 255, 255, 0.05);
      border-radius: 10px;
      animation: fade-in 1.5s ease-out 1.3s both;
    }
    
    .info-item {
      padding: 10px;
      border-left: 3px solid #00ff88;
      text-align: left;
    }
    
    .info-label {
      font-size: 0.9em;
      color: #00ff88;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .info-value {
      font-size: 1.1em;
      color: #00ffff;
      margin-top: 5px;
      word-break: break-all;
    }
    
    @keyframes fade-in {
      from {
        opacity: 0;
        transform: translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    
    @media (max-width: 768px) {
      .container {
        width: 90%;
        padding: 30px;
      }
      
      h1 {
        font-size: 1.8em;
      }
      
      .subtitle {
        font-size: 1.1em;
      }
      
      .profile-info {
        grid-template-columns: 1fr;
      }
      
      .btn {
        padding: 12px 25px;
        font-size: 1em;
      }
    }
  </style>
</head>
<body>
  <canvas id="matrix"></canvas>
  <div class="container">
    <h1>Salom! 👋</h1>
    <p class="subtitle">Bu Shamsiddinov Habibullo ning web sahifasi</p>
    
    <div class="profile-info">
      <div class="info-item">
        <div class="info-label">📝 Ism</div>
        <div class="info-value">Shamsiddinov Habibullo</div>
      </div>
      <div class="info-item">
        <div class="info-label">💻 Kasb</div>
        <div class="info-value">Full Stack Developer</div>
      </div>
      <div class="info-item">
        <div class="info-label">📍 Joylashuvi</div>
        <div class="info-value">Tashkent, O'zbekiston</div>
      </div>
      <div class="info-item">
        <div class="info-label">🎯 Maqsadi</div>
        <div class="info-value">Dastur yaratish</div>
      </div>
    </div>
    
    <div class="contact-section">
      <div class="contact-title">> Meni Bilan Bog'laning</div>
      <p>
        Telegram orqali bog'laning:
        <a href="https://t.me/khabib0609" target="_blank">@khabib0609</a>
      </p>
      <p>
        Email:
        <a href="mailto:habibullo@gmail.com">habibullo@gmail.com</a>
      </p>
      <p>
        GitHub:
        <a href="https://github.com/habibullo" target="_blank">github.com/habibullo</a>
      </p>
      <p>
        LinkedIn:
        <a href="https://linkedin.com/in/habibullo" target="_blank">linkedin.com/in/habibullo</a>
      </p>
    </div>
    
    <a class="btn" href="https://t.me/khabib0609" target="_blank">📱 Telegram da Bog'lanish</a>
  </div>

  <script>
    const canvas = document.getElementById("matrix");
    const ctx = canvas.getContext("2d");
    
    function resizeCanvas() {
      canvas.height = window.innerHeight;
      canvas.width = window.innerWidth;
    }
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);
    
    const letters = "01";
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = [];
    
    for (let i = 0; i < columns; i++) {
      drops[i] = Math.random() * canvas.height;
    }
    
    function draw() {
      ctx.fillStyle = "rgba(0, 0, 0, 0.08)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Ko'k va yashil ranglar
      const colors = ["#00ffff", "#00ff88"];
      
      ctx.font = fontSize + "px monospace";
      
      for (let i = 0; i < drops.length; i++) {
        // Random rangi
        const colorIndex = Math.random() > 0.5 ? 0 : 1;
        ctx.fillStyle = colors[colorIndex];
        
        const text = letters.charAt(Math.floor(Math.random() * letters.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        // Agar pastga tushib ketsa, yangi boshlanadi
        if (drops[i] * fontSize > canvas.height) {
          drops[i] = 0;
        }
        
        drops[i]++;
      }
    }
    
    // Animatsiya
    setInterval(draw, 35);
  </script>
</body>
</html>
