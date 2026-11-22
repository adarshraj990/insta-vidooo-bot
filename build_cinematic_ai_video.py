import os

html_code = '''<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<title>Mohabbat Si Zamana Si — Cinematic Mughal Miniature</title>
<link rel="stylesheet" href="fonts.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 720px;
    height: 1280px;
    overflow: hidden;
    background: #060205;
    font-family: 'Noto Serif Devanagari', serif;
    -webkit-font-smoothing: antialiased;
  }
  #stage {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
  }
  #paper-canvas, #fx-canvas {
    position: absolute;
    left: 0; top: 0;
    width: 720px; height: 1280px;
    pointer-events: none;
  }
  #paper-canvas {
    mix-blend-mode: multiply;
    opacity: 0.15;
  }
  #fx-canvas {
    mix-blend-mode: screen;
  }
</style>
</head>
<body>

<svg id="stage" viewBox="0 0 720 1280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Antique Gold Foil Gradient -->
    <linearGradient id="grad-gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#805C15"/>
      <stop offset="25%" stop-color="#CFA138"/>
      <stop offset="50%" stop-color="#FFF3B0"/>
      <stop offset="75%" stop-color="#CFA138"/>
      <stop offset="100%" stop-color="#6E4D0C"/>
    </linearGradient>

    <!-- Warm Vignette for Cinematic Depth -->
    <radialGradient id="grad-vignette" cx="50%" cy="50%" r="50%">
      <stop offset="60%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.65"/>
    </radialGradient>
  </defs>

  <!-- ================= SCENE 1: THE SUNSET JHAROKHA & ROSE (0.0s - 4.5s) ================= -->
  <!-- "मोहब्बत सी, ज़माना सी" -->
  <g id="scene-1" opacity="1">
    <g id="cam-1">
      <image href="assets/scene1.jpg" x="-24" y="-48" width="768" height="1376" preserveAspectRatio="xMidYMid slice"/>
    </g>
  </g>

  <!-- ================= SCENE 2: THE DEVOTED HEART & LOVE LETTER (4.5s - 8.8s) ================= -->
  <!-- "यह दिल तेरा दीवाना सी" -->
  <g id="scene-2" opacity="0">
    <g id="cam-2">
      <image href="assets/scene2.jpg" x="-24" y="-48" width="768" height="1376" preserveAspectRatio="xMidYMid slice"/>
    </g>
  </g>

  <!-- ================= SCENE 3: COLD MIDNIGHT RAIN & SCATTERED PETALS (8.8s - 13.5s) ================= -->
  <!-- "मेरा यह हाल होना सी" -->
  <g id="scene-3" opacity="0">
    <g id="cam-3">
      <image href="assets/scene3.jpg" x="-24" y="-48" width="768" height="1376" preserveAspectRatio="xMidYMid slice"/>
    </g>
  </g>

  <!-- ================= SCENE 4: CRESCENT MOON & HOURGLASS OF FATE (13.5s - 18.17s) ================= -->
  <!-- "तेरा मिलना बहाना सी..." -->
  <g id="scene-4" opacity="0">
    <g id="cam-4">
      <image href="assets/scene4.jpg" x="-24" y="-48" width="768" height="1376" preserveAspectRatio="xMidYMid slice"/>
    </g>
  </g>

  <!-- ================= ROYAL CINEMATIC FRAME & VIGNETTE ================= -->
  <!-- Subtle Vignette -->
  <rect width="720" height="1280" fill="url(#grad-vignette)" pointer-events="none"/>

  <!-- Ornate Mughal Miniature Border (Hasliya) -->
  <g id="frame-border" pointer-events="none">
    <rect x="18" y="18" width="684" height="1244" fill="none" stroke="url(#grad-gold)" stroke-width="2.5"/>
    <rect x="25" y="25" width="670" height="1230" fill="none" stroke="#FFE885" stroke-width="1" stroke-dasharray="8,6" opacity="0.6"/>
    <!-- Four Ornate Corner Ornaments -->
    <path d="M 18,38 L 38,18 M 18,48 L 48,18" stroke="url(#grad-gold)" stroke-width="1.8"/>
    <path d="M 702,38 L 682,18 M 702,48 L 672,18" stroke="url(#grad-gold)" stroke-width="1.8"/>
    <path d="M 18,1242 L 38,1262 M 18,1232 L 48,1262" stroke="url(#grad-gold)" stroke-width="1.8"/>
    <path d="M 702,1242 L 682,1262 M 702,1232 L 672,1262" stroke="url(#grad-gold)" stroke-width="1.8"/>
  </g>

  <!-- ================= MASTER SUBTITLE CARDS (0.0s - 18.17s) ================= -->
  <g id="subtitles">
    <!-- Subtitle 1 (0.2s - 4.4s) -->
    <g id="sub-1" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="14" fill="rgba(14, 5, 10, 0.94)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        मोहब्बत सी, ज़माना सी
      </text>
      <text x="250" y="90" fill="#FFA726" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        MOHABBAT SI, ZAMANA SI
      </text>
      <text x="250" y="118" fill="#CFA138" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // AN ERA OF ETERNAL LOVE
      </text>
    </g>

    <!-- Subtitle 2 (4.5s - 8.7s) -->
    <g id="sub-2" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="14" fill="rgba(14, 5, 10, 0.94)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        यह दिल तेरा दीवाना सी
      </text>
      <text x="250" y="90" fill="#FF5252" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        YEH DIL TERA DEEWANA SI
      </text>
      <text x="250" y="118" fill="#CFA138" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // THIS HEART WAS CRAZY FOR YOU
      </text>
    </g>

    <!-- Subtitle 3 (8.8s - 13.4s) -->
    <g id="sub-3" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="14" fill="rgba(8, 16, 28, 0.95)" stroke="#90CAF9" stroke-width="2.5"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        मेरा यह हाल होना सी...
      </text>
      <text x="250" y="90" fill="#90CAF9" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        MERA YEH HAAL HONA SI
      </text>
      <text x="250" y="118" fill="#64B5F6" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // THIS RUIN WAS WRITTEN BY FATE
      </text>
    </g>

    <!-- Subtitle 4 (13.5s - 18.17s) -->
    <g id="sub-4" transform="translate(110, 800)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="14" fill="rgba(14, 6, 12, 0.95)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        तेरा मिलना बहाना सी...
      </text>
      <text x="250" y="90" fill="#FFE082" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        TERA MILNA BAHANA SI
      </text>
      <text x="250" y="118" fill="#CFA138" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // MEETING YOU WAS BUT DESTINY\'S PRETEXT
      </text>
    </g>
  </g>
</svg>

<canvas id="paper-canvas" width="720" height="1280"></canvas>
<canvas id="fx-canvas" width="720" height="1280"></canvas>

<script>
const DUR = 18.17;
window.DUR = DUR;

const fxCanvas = document.getElementById('fx-canvas');
const ctx = fxCanvas.getContext('2d');

function pseudoRand(seed) {
  const x = Math.sin(seed * 9999.123) * 10000;
  return x - Math.floor(x);
}

// 1. Handmade Cotton Rag Paper Texture Overlay
function initPaperTexture() {
  const pCan = document.getElementById('paper-canvas');
  const pCtx = pCan.getContext('2d');
  const imgData = pCtx.createImageData(720, 1280);
  const data = imgData.data;

  for (let i = 0; i < data.length; i += 4) {
    const n = Math.random();
    const val = Math.floor(225 + n * 30);
    data[i] = val;
    data[i+1] = Math.floor(val * 0.96);
    data[i+2] = Math.floor(val * 0.88);
    data[i+3] = 255;
  }
  pCtx.putImageData(imgData, 0, 0);
}

// 2. Dynamic Atmosphere FX (Golden Motes, Silver Rain, Drifting Petals)
function drawFX(t) {
  ctx.clearRect(0, 0, 720, 1280);

  if (t < 8.8) {
    // Act 1 & 2: Floating Golden Dust Motes & Embers
    const numMotes = 32;
    for (let i = 0; i < numMotes; i++) {
      const seed = i + 1;
      const baseX = 80 + pseudoRand(seed * 17) * 560;
      const baseY = 180 + pseudoRand(seed * 23) * 850;
      const spdY = 16 + pseudoRand(seed * 31) * 24;
      const curY = (baseY - t * spdY) % 850 + 180;
      const curX = baseX + Math.sin(t * 2 + seed) * 16;
      const sz = 1.4 + pseudoRand(seed * 41) * 2.2;
      const a = 0.35 + 0.55 * Math.sin(t * 3.2 + seed * 2);

      ctx.beginPath();
      ctx.arc(curX, curY, sz, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 225, 130, ${Math.max(0, a).toFixed(2)})`;
      ctx.fill();
    }
  } else if (t < 13.5) {
    // Act 3: Diagonal Cold Rain Streaks
    const numRain = 95;
    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'rgba(175, 220, 255, 0.45)';
    for (let i = 0; i < numRain; i++) {
      const seed = i + 1;
      const rx = (seed * 137.5 + t * 480) % 760 - 20;
      const ry = (seed * 219.3 + t * 980) % 1320 - 20;
      const len = 35 + pseudoRand(seed * 43) * 35;

      ctx.beginPath();
      ctx.moveTo(rx, ry);
      ctx.lineTo(rx - len * 0.35, ry + len);
      ctx.stroke();
    }
  } else {
    // Act 4: Drifting Velvet Rose Petals
    const numPetals = 20;
    for (let i = 0; i < numPetals; i++) {
      const seed = i + 1;
      const px = 80 + pseudoRand(seed * 29) * 560 + Math.sin(t * 1.6 + seed) * 35;
      const py = (180 + (t - 13.5) * (35 + pseudoRand(seed * 13) * 35) + seed * 55) % 1000 + 100;
      const rot = t * 2.2 + seed;

      ctx.save();
      ctx.translate(px, py);
      ctx.rotate(rot);
      ctx.beginPath();
      ctx.ellipse(0, 0, 7.5, 4.8, 0, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(215, 25, 75, 0.75)';
      ctx.fill();
      ctx.restore();
    }
  }
}

// 3. Main Render Function with Ken Burns Camera & Dissolves
function render(t) {
  t = Math.max(0, Math.min(t, DUR));

  const s1 = document.getElementById('scene-1');
  const s2 = document.getElementById('scene-2');
  const s3 = document.getElementById('scene-3');
  const s4 = document.getElementById('scene-4');

  const cam1 = document.getElementById('cam-1');
  const cam2 = document.getElementById('cam-2');
  const cam3 = document.getElementById('cam-3');
  const cam4 = document.getElementById('cam-4');

  const sub1 = document.getElementById('sub-1');
  const sub2 = document.getElementById('sub-2');
  const sub3 = document.getElementById('sub-3');
  const sub4 = document.getElementById('sub-4');

  // Scene 1: (0.0s - 4.5s)
  if (t < 4.5) {
    s1.style.display = 'inline';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Ken Burns gentle push-in towards the lovers holding the rose
    const p1 = t / 4.5;
    const sc1 = 1.0 + 0.06 * p1;
    const tx1 = -24 - (sc1 - 1.0) * 360;
    const ty1 = -48 - (sc1 - 1.0) * 640;
    cam1.setAttribute('transform', `translate(${tx1.toFixed(1)}, ${ty1.toFixed(1)}) scale(${sc1.toFixed(4)})`);

    if (t > 4.1) {
      const outP = (t - 4.1) / 0.4;
      s1.setAttribute('opacity', (1 - outP).toFixed(2));
    } else {
      s1.setAttribute('opacity', '1');
    }
  } else if (t < 8.8) {
    // Scene 2: (4.5s - 8.8s)
    s1.style.display = 'none';
    s2.style.display = 'inline';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Ken Burns intimate pan + heartbeat breathing pulse
    const p2 = (t - 4.5) / 4.3;
    const beat = 0.015 * Math.sin(t * 6.2);
    const sc2 = 1.03 + 0.04 * p2 + beat;
    const tx2 = -24 - (sc2 - 1.0) * 360;
    const ty2 = -48 - (sc2 - 1.0) * 580;
    cam2.setAttribute('transform', `translate(${tx2.toFixed(1)}, ${ty2.toFixed(1)}) scale(${sc2.toFixed(4)})`);

    if (t < 4.9) {
      const inP = (t - 4.5) / 0.4;
      s2.setAttribute('opacity', inP.toFixed(2));
    } else if (t > 8.4) {
      const outP = (t - 8.4) / 0.4;
      s2.setAttribute('opacity', (1 - outP).toFixed(2));
    } else {
      s2.setAttribute('opacity', '1');
    }
  } else if (t < 13.5) {
    // Scene 3: (8.8s - 13.5s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'inline';
    s4.style.display = 'none';

    // Ken Burns sorrowful drift downward revealing the fallen petals on marble
    const p3 = (t - 8.8) / 4.7;
    const sc3 = 1.05 - 0.03 * p3;
    const tx3 = -24 - (sc3 - 1.0) * 360;
    const ty3 = -48 - (sc3 - 1.0) * 640 + p3 * 22;
    cam3.setAttribute('transform', `translate(${tx3.toFixed(1)}, ${ty3.toFixed(1)}) scale(${sc3.toFixed(4)})`);

    if (t < 9.2) {
      const inP = (t - 8.8) / 0.4;
      s3.setAttribute('opacity', inP.toFixed(2));
    } else if (t > 13.1) {
      const outP = (t - 13.1) / 0.4;
      s3.setAttribute('opacity', (1 - outP).toFixed(2));
    } else {
      s3.setAttribute('opacity', '1');
    }
  } else {
    // Scene 4: (13.5s - 18.17s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'inline';

    // Ken Burns slow pan down from the crescent moon to the hourglass
    const p4 = (t - 13.5) / (18.17 - 13.5);
    const sc4 = 1.02 + 0.04 * p4;
    const tx4 = -24 - (sc4 - 1.0) * 360;
    const ty4 = -48 - (sc4 - 1.0) * 640 + (p4 - 0.5) * 25;
    cam4.setAttribute('transform', `translate(${tx4.toFixed(1)}, ${ty4.toFixed(1)}) scale(${sc4.toFixed(4)})`);

    if (t < 13.9) {
      const inP = (t - 13.5) / 0.4;
      s4.setAttribute('opacity', inP.toFixed(2));
    } else {
      s4.setAttribute('opacity', '1');
    }
  }

  // Master Subtitle Card Timing
  if (t >= 0.2 && t < 4.4) {
    const pIn = Math.min(1, (t - 0.2) / 0.35);
    const pOut = t > 4.0 ? Math.max(0, (4.4 - t) / 0.4) : 1;
    sub1.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub1.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub1.setAttribute('opacity', '0');
  }

  if (t >= 4.5 && t < 8.7) {
    const pIn = Math.min(1, (t - 4.5) / 0.35);
    const pOut = t > 8.3 ? Math.max(0, (8.7 - t) / 0.4) : 1;
    sub2.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub2.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub2.setAttribute('opacity', '0');
  }

  if (t >= 8.8 && t < 13.4) {
    const pIn = Math.min(1, (t - 8.8) / 0.35);
    const pOut = t > 13.0 ? Math.max(0, (13.4 - t) / 0.4) : 1;
    sub3.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub3.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub3.setAttribute('opacity', '0');
  }

  if (t >= 13.5 && t <= 18.17) {
    const pIn = Math.min(1, (t - 13.5) / 0.35);
    sub4.setAttribute('opacity', pIn.toFixed(2));
    sub4.setAttribute('transform', `translate(110, ${(810 - pIn * 10).toFixed(1)})`);
  } else {
    sub4.setAttribute('opacity', '0');
  }

  drawFX(t);
}

// 4. TEXTS contract for readcheck.mjs
window.TEXTS = function(t) {
  const texts = [];

  if (t >= 0.2 && t < 4.4) {
    texts.push({
      id: 'sub_strophe_1',
      text: 'मोहब्बत सी, ज़माना सी',
      x0: 110, y0: 980, x1: 610, y1: 1120
    });
  }

  if (t >= 4.5 && t < 8.7) {
    texts.push({
      id: 'sub_strophe_2',
      text: 'यह दिल तेरा दीवाना सी',
      x0: 110, y0: 980, x1: 610, y1: 1120
    });
  }

  if (t >= 8.8 && t < 13.4) {
    texts.push({
      id: 'sub_strophe_3',
      text: 'मेरा यह हाल होना सी',
      x0: 110, y0: 980, x1: 610, y1: 1120
    });
  }

  if (t >= 13.5 && t <= 18.17) {
    texts.push({
      id: 'sub_strophe_4',
      text: 'तेरा मिलना बहाना सी',
      x0: 110, y0: 800, x1: 610, y1: 940
    });
  }

  return texts;
};

// 5. Preloading & Initialization
async function init() {
  initPaperTexture();

  // Preload all 4 scene images
  const imgs = ['assets/scene1.jpg', 'assets/scene2.jpg', 'assets/scene3.jpg', 'assets/scene4.jpg'];
  await Promise.all(imgs.map(src => new Promise(res => {
    const im = new Image();
    im.onload = res;
    im.onerror = res;
    im.src = src;
  })));

  // Load typography fonts
  const fams = [
    '700 32px "Noto Serif Devanagari"',
    '400 32px "Noto Serif Devanagari"',
    '600 16px "JetBrains Mono"'
  ];
  const sample = 'मोहब्बतसीज़मानायहदिलतेरादीवानामेराहालहोनामिलनाबहानाABCDEFGHIJKLMNOPQRSTUVWXYZ//:[]';
  await Promise.all(fams.map(f => document.fonts.load(f, sample)));
  await document.fonts.ready;

  const q = new URLSearchParams(location.search);
  render(parseFloat(q.get('t') || '0'));
  window.READY = true;
}

window.render = render;
init();
</script>
</body>
</html>
'''

with open(r'c:\Users\Adarsh\Desktop\vidooo\mohabbat-si\index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('Updated index.html with Cinematic AI Artwork! Length:', len(html_code))
