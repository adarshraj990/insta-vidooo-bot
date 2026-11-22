import json

html_template = """<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<title>Hum Tadapte Rahenge Yahan Raat Bhar — Mughal Miniature Cinema</title>
<link rel="stylesheet" href="fonts.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 720px;
    height: 1280px;
    overflow: hidden;
    background: #05080E;
    font-family: 'Noto Serif Devanagari', serif;
    -webkit-font-smoothing: antialiased;
  }
  #stage {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
    overflow: hidden;
  }
  .scene-layer {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
    opacity: 0;
    transition: opacity 0.4s ease-in-out;
    will-change: transform, opacity;
  }
  .scene-layer img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
  #paper-canvas, #fx-canvas {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
    pointer-events: none;
  }
  #paper-canvas {
    mix-blend-mode: multiply;
    opacity: 0.18;
  }
  #fx-canvas {
    mix-blend-mode: screen;
  }
  #frame-overlay {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
    pointer-events: none;
  }
  #caption-box {
    position: absolute;
    left: 40px;
    bottom: 95px;
    width: 640px;
    text-align: center;
    pointer-events: none;
    z-index: 100;
  }
  .card-bg {
    display: inline-block;
    padding: 18px 32px 14px 32px;
    background: rgba(10, 14, 22, 0.72);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 25px rgba(212, 175, 55, 0.2);
  }
  .main-text {
    font-size: 32px;
    font-weight: 700;
    color: #FFFDF8;
    line-height: 1.35;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.9), 0 0 20px rgba(255, 215, 0, 0.4);
  }
  .trans-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 500;
    color: #D4AF37;
    margin-top: 8px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    text-shadow: 0 1px 4px rgba(0,0,0,0.9);
  }
  .act-indicator {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: rgba(255, 255, 255, 0.65);
    letter-spacing: 2px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<div id="stage">
  <!-- 4 Scene Layers -->
  <div id="scene-1" class="scene-layer"><img id="img-scene-1" src="assets/scene1.jpg" alt="Scene 1"></div>
  <div id="scene-2" class="scene-layer"><img id="img-scene-2" src="assets/scene2.jpg" alt="Scene 2"></div>
  <div id="scene-3" class="scene-layer"><img id="img-scene-3" src="assets/scene3.jpg" alt="Scene 3"></div>
  <div id="scene-4" class="scene-layer"><img id="img-scene-4" src="assets/scene4.jpg" alt="Scene 4"></div>

  <!-- Dynamic Particle FX Canvas -->
  <canvas id="fx-canvas" width="720" height="1280"></canvas>

  <!-- Handmade Indian Paper Texture Overlay -->
  <canvas id="paper-canvas" width="720" height="1280"></canvas>

  <!-- Royal Mughal Hasliya Gold Border SVG -->
  <svg id="frame-overlay" viewBox="0 0 720 1280" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="gold-grad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#BF953F"/>
        <stop offset="25%" stop-color="#FCF6BA"/>
        <stop offset="50%" stop-color="#B38728"/>
        <stop offset="75%" stop-color="#FBF5B7"/>
        <stop offset="100%" stop-color="#AA771C"/>
      </linearGradient>
    </defs>
    <!-- Outer Border -->
    <rect x="14" y="14" width="692" height="1252" fill="none" stroke="url(#gold-grad)" stroke-width="2.5" opacity="0.85"/>
    <rect x="22" y="22" width="676" height="1236" fill="none" stroke="#D4AF37" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>
    <rect x="26" y="26" width="668" height="1228" fill="none" stroke="url(#gold-grad)" stroke-width="0.8" opacity="0.5"/>
    
    <!-- 4 Corner Ornaments -->
    <g stroke="url(#gold-grad)" fill="none" stroke-width="1.5">
      <!-- TL -->
      <path d="M 22 55 L 55 22 M 22 40 L 40 22 M 22 22 L 32 32"/>
      <circle cx="38" cy="38" r="4" fill="#D4AF37"/>
      <!-- TR -->
      <path d="M 698 55 L 665 22 M 698 40 L 680 22 M 698 22 L 688 32"/>
      <circle cx="682" cy="38" r="4" fill="#D4AF37"/>
      <!-- BL -->
      <path d="M 22 1225 L 55 1258 M 22 1240 L 40 1258 M 22 1258 L 32 1248"/>
      <circle cx="38" cy="1242" r="4" fill="#D4AF37"/>
      <!-- BR -->
      <path d="M 698 1225 L 665 1258 M 698 1240 L 680 1258 M 698 1258 L 688 1248"/>
      <circle cx="682" cy="1242" r="4" fill="#D4AF37"/>
    </g>
  </svg>

  <!-- Typography Card -->
  <div id="caption-box">
    <div class="card-bg">
      <div id="sub-indicator" class="act-indicator">अंक I • साँझ की विदा</div>
      <div id="sub-main" class="main-text">मत जाओ ना बेचैन करके मुझे...</div>
      <div id="sub-trans" class="trans-text">Mat jao na bechain karke mujhe...</div>
    </div>
  </div>
</div>

<script>
window.DUR = 20.01;
window.FPS = 30;
window.READY = false;

const TIMELINE = [
  {
    id: 1,
    start: 0.0,
    end: 5.5,
    indicator: "अंक I • साँझ की विदा",
    main: "मत जाओ ना बेचैन करके मुझे, जाने-जाँ दिल दुखाना बुरी बात है...",
    trans: "Mat jao na bechain karke mujhe, jaane-jaan dil dukhana buri baat hai...",
    domId: "scene-1",
    camera: (prog) => {
      const scale = 1.05 + prog * 0.06;
      const x = -prog * 20;
      const y = -prog * 35;
      return `scale(${scale}) translate(${x}px, ${y}px)`;
    }
  },
  {
    id: 2,
    start: 5.5,
    end: 10.5,
    indicator: "अंक II • विरह की रात",
    main: "हम तड़पते रहेंगे यहाँ रात भर...",
    trans: "Hum tadapte rahenge yahan raat bhar...",
    domId: "scene-2",
    camera: (prog) => {
      const scale = 1.04 + prog * 0.08;
      const x = -prog * 15;
      const y = -prog * 20;
      return `scale(${scale}) translate(${x}px, ${y}px)`;
    }
  },
  {
    id: 3,
    start: 10.5,
    end: 15.5,
    indicator: "अंक III • बेख़बर नींद",
    main: "तुम तो आराम की नींद सो जाओगे...",
    trans: "Tum to aaram ki neend so jaoge...",
    domId: "scene-3",
    camera: (prog) => {
      const scale = 1.05 + prog * 0.05;
      const x = prog * 15;
      const y = prog * 20;
      return `scale(${scale}) translate(${x}px, ${y}px)`;
    }
  },
  {
    id: 4,
    start: 15.5,
    end: 20.01,
    indicator: "अंक IV • बारिश और तन्हाई",
    main: "हम तड़पते रहेंगे यहाँ रात भर...",
    trans: "Hum tadapte rahenge yahan raat bhar...",
    domId: "scene-4",
    camera: (prog) => {
      const scale = 1.03 + prog * 0.07;
      const x = prog * 10;
      const y = -prog * 25;
      return `scale(${scale}) translate(${x}px, ${y}px)`;
    }
  }
];

// Pre-render Paper Texture Canvas
const paperCanvas = document.getElementById("paper-canvas");
const pctx = paperCanvas.getContext("2d");
function drawPaper() {
  const w = 720, h = 1280;
  pctx.fillStyle = "#FAF5E9";
  pctx.fillRect(0, 0, w, h);
  const imgData = pctx.getImageData(0, 0, w, h);
  const d = imgData.data;
  let seed = 42;
  function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  for (let i = 0; i < d.length; i += 4) {
    const noise = (rnd() - 0.5) * 28;
    d[i] = Math.min(255, Math.max(0, d[i] + noise));
    d[i+1] = Math.min(255, Math.max(0, d[i+1] + noise));
    d[i+2] = Math.min(255, Math.max(0, d[i+2] + noise));
  }
  pctx.putImageData(imgData, 0, 0);
}
drawPaper();

// Dynamic FX Canvas (Golden motes, rain, petals)
const fxCanvas = document.getElementById("fx-canvas");
const fctx = fxCanvas.getContext("2d");

const PARTICLES = [];
for (let i = 0; i < 90; i++) {
  PARTICLES.push({
    x: (i * 97) % 720,
    y: (i * 131) % 1280,
    r: 1.2 + (i % 5) * 0.8,
    speedY: 25 + (i % 7) * 8,
    speedX: (i % 2 === 0 ? 1 : -1) * (10 + (i % 4) * 5),
    alpha: 0.35 + (i % 6) * 0.1
  });
}

const PETALS = [];
for (let i = 0; i < 28; i++) {
  PETALS.push({
    x: (i * 123) % 720,
    y: (i * 211) % 1280,
    rx: 6 + (i % 5) * 2,
    ry: 10 + (i % 6) * 2,
    rot: (i * 45) * Math.PI / 180,
    speedY: 60 + (i % 5) * 15,
    speedX: 20 + (i % 4) * 10,
    alpha: 0.65 + (i % 4) * 0.1
  });
}

function renderFX(t) {
  fctx.clearRect(0, 0, 720, 1280);
  if (t < 15.5) {
    for (let p of PARTICLES) {
      const curY = (p.y + p.speedY * t) % 1280;
      const curX = (p.x + Math.sin(t * 1.5 + p.r) * 25 + 720) % 720;
      fctx.beginPath();
      fctx.arc(curX, curY, p.r, 0, Math.PI * 2);
      fctx.fillStyle = `rgba(255, 220, 120, ${p.alpha})`;
      fctx.shadowColor = "rgba(255, 215, 0, 0.6)";
      fctx.shadowBlur = 6;
      fctx.fill();
    }
  } else {
    fctx.strokeStyle = "rgba(180, 210, 240, 0.4)";
    fctx.lineWidth = 1.2;
    fctx.beginPath();
    for (let i = 0; i < 70; i++) {
      const rx = (i * 83 + t * 140) % 720;
      const ry = (i * 107 + t * 950) % 1280;
      fctx.moveTo(rx, ry);
      fctx.lineTo(rx - 12, ry + 42);
    }
    fctx.stroke();

    for (let pet of PETALS) {
      const curY = (pet.y + pet.speedY * (t - 15.5)) % 1280;
      const curX = (pet.x + Math.sin((t - 15.5) * 2 + pet.rx) * 35 + 720) % 720;
      fctx.save();
      fctx.translate(curX, curY);
      fctx.rotate(pet.rot + t * 1.2);
      fctx.beginPath();
      fctx.ellipse(0, 0, pet.rx, pet.ry, 0, 0, Math.PI * 2);
      fctx.fillStyle = `rgba(180, 20, 35, ${pet.alpha})`;
      fctx.shadowColor = "rgba(100, 0, 15, 0.6)";
      fctx.shadowBlur = 4;
      fctx.fill();
      fctx.restore();
    }
  }
}

// TEXTS Contract for readcheck.mjs
window.TEXTS = function(t) {
  const texts = [];
  if (t >= 0.2 && t < 5.4) {
    texts.push({
      id: 'sub_strophe_1',
      text: 'मत जाओ ना बेचैन करके मुझे',
      x0: 40, y0: 950, x1: 680, y1: 1200
    });
  }
  if (t >= 5.5 && t < 10.4) {
    texts.push({
      id: 'sub_strophe_2',
      text: 'हम तड़पते रहेंगे यहाँ रात भर',
      x0: 40, y0: 950, x1: 680, y1: 1200
    });
  }
  if (t >= 10.5 && t < 15.4) {
    texts.push({
      id: 'sub_strophe_3',
      text: 'तुम तो आराम की नींद सो जाओगे',
      x0: 40, y0: 950, x1: 680, y1: 1200
    });
  }
  if (t >= 15.5 && t <= 20.01) {
    texts.push({
      id: 'sub_strophe_4',
      text: 'हम तड़पते रहेंगे यहाँ रात भर',
      x0: 40, y0: 950, x1: 680, y1: 1200
    });
  }
  return texts;
};

// Frame Seek Function
window.setSeek = function(t) {
  t = Math.max(0, Math.min(window.DUR, t));
  
  let activeAct = TIMELINE[0];
  for (let act of TIMELINE) {
    if (t >= act.start && t < act.end) {
      activeAct = act;
      break;
    }
  }
  if (t >= TIMELINE[TIMELINE.length - 1].end - 0.05) {
    activeAct = TIMELINE[TIMELINE.length - 1];
  }

  for (let act of TIMELINE) {
    const el = document.getElementById(act.domId);
    if (!el) continue;
    let opacity = 0;
    if (t >= act.start && t < act.end) {
      const fadeDuration = 0.4;
      if (t - act.start < fadeDuration && act.id > 1) {
        opacity = (t - act.start) / fadeDuration;
      } else {
        opacity = 1;
      }
      const progress = (t - act.start) / (act.end - act.start);
      el.style.transform = act.camera(progress);
    } else {
      opacity = 0;
    }
    el.style.opacity = opacity;
  }

  document.getElementById("sub-indicator").textContent = activeAct.indicator;
  document.getElementById("sub-main").textContent = activeAct.main;
  document.getElementById("sub-trans").textContent = activeAct.trans;

  renderFX(t);
};
window.render = window.setSeek;


// Image Preloader
const imageSources = [
  "assets/scene1.jpg",
  "assets/scene2.jpg",
  "assets/scene3.jpg",
  "assets/scene4.jpg"
];

let loadedCount = 0;
imageSources.forEach(src => {
  const img = new Image();
  img.onload = () => {
    loadedCount++;
    if (loadedCount === imageSources.length) {
      window.setSeek(0);
      window.READY = true;
    }
  };
  img.onerror = () => {
    loadedCount++;
    if (loadedCount === imageSources.length) {
      window.setSeek(0);
      window.READY = true;
    }
  };
  img.src = src;
});
</script>

</body>
</html>
"""

with open('c:/Users/Adarsh/Desktop/vidooo/hum-tadapte/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Updated index.html with window.TEXTS!")
