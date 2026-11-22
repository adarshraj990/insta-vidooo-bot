import os

html_code = '''<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<title>Mohabbat Si Zamana Si — Mughal Miniature Storybook (Masterpiece Edition)</title>
<link rel="stylesheet" href="fonts.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 720px;
    height: 1280px;
    overflow: hidden;
    background: #0D040A;
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
    opacity: 0.18;
  }
  #fx-canvas {
    mix-blend-mode: screen;
  }
</style>
</head>
<body>

<svg id="stage" viewBox="0 0 720 1280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Warm Golden Hour Sunset Gradient -->
    <linearGradient id="grad-sunset-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4A0B1A"/>
      <stop offset="30%" stop-color="#8C1D2A"/>
      <stop offset="60%" stop-color="#D95328"/>
      <stop offset="85%" stop-color="#FCA33C"/>
      <stop offset="100%" stop-color="#FFF3A8"/>
    </linearGradient>

    <!-- Sandstone Palace Wall Gradient -->
    <linearGradient id="grad-sandstone" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E5BE90"/>
      <stop offset="50%" stop-color="#CE9F6A"/>
      <stop offset="100%" stop-color="#AF7E4C"/>
    </linearGradient>

    <!-- Midnight Stone Palace Wall Gradient -->
    <linearGradient id="grad-night-stone" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#24384D"/>
      <stop offset="50%" stop-color="#182A3A"/>
      <stop offset="100%" stop-color="#0E1A26"/>
    </linearGradient>

    <!-- Polished Makrana Marble -->
    <linearGradient id="grad-marble" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F2EDE4"/>
      <stop offset="100%" stop-color="#DED7C8"/>
    </linearGradient>

    <!-- Pure Antique Gold Leaf -->
    <linearGradient id="grad-gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#805C15"/>
      <stop offset="25%" stop-color="#CFA138"/>
      <stop offset="50%" stop-color="#FFF3B0"/>
      <stop offset="75%" stop-color="#CFA138"/>
      <stop offset="100%" stop-color="#6E4D0C"/>
    </linearGradient>

    <!-- Warm Lantern Radiant Halo -->
    <radialGradient id="grad-lantern-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFDE0" stop-opacity="1"/>
      <stop offset="25%" stop-color="#FFB326" stop-opacity="0.85"/>
      <stop offset="65%" stop-color="#E64A19" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#E64A19" stop-opacity="0"/>
    </radialGradient>

    <!-- Midnight Royal Sky Gradient -->
    <linearGradient id="grad-night-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#08101E"/>
      <stop offset="35%" stop-color="#0F2035"/>
      <stop offset="70%" stop-color="#1A3450"/>
      <stop offset="100%" stop-color="#284B6E"/>
    </linearGradient>

    <!-- Silver Crescent Moon Radiance -->
    <radialGradient id="grad-moon-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="30%" stop-color="#E2F1FD" stop-opacity="0.75"/>
      <stop offset="65%" stop-color="#90CAF9" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0A182B" stop-opacity="0"/>
    </radialGradient>

    <!-- Rose Petal Velvet Shading -->
    <radialGradient id="grad-rose" cx="40%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#FF4D6D"/>
      <stop offset="50%" stop-color="#C9184A"/>
      <stop offset="100%" stop-color="#590D22"/>
    </radialGradient>

    <!-- Jewels -->
    <radialGradient id="grad-emerald" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#6EE7B7"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#064E3B"/>
    </radialGradient>

    <radialGradient id="grad-ruby" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FDA4AF"/>
      <stop offset="50%" stop-color="#E11D48"/>
      <stop offset="100%" stop-color="#881337"/>
    </radialGradient>

    <radialGradient id="grad-pearl" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="65%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#94A3B8"/>
    </radialGradient>

    <!-- Silk Fabrics -->
    <linearGradient id="grad-prince-robe" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="45%" stop-color="#FFF8E7"/>
      <stop offset="100%" stop-color="#DECCA6"/>
    </linearGradient>

    <linearGradient id="grad-princess-sleeve" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C9184A"/>
      <stop offset="50%" stop-color="#800F2F"/>
      <stop offset="100%" stop-color="#590D22"/>
    </linearGradient>

    <!-- Vintage Love Letter Parchment -->
    <linearGradient id="grad-letter" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="50%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#EAD79D"/>
    </linearGradient>
  </defs>

  <!-- ================= SCENE 1: THE SUNSET JHAROKHA & ROSE (0.0s - 4.5s) ================= -->
  <!-- "मोहब्बत सी, ज़माना सी" -->
  <g id="scene-1" opacity="1">
    <rect width="720" height="1280" fill="url(#grad-sunset-sky)"/>
    
    <!-- Distant Mughal Palace Domes Silhouette -->
    <g fill="#3B0818" opacity="0.65">
      <path d="M 0,620 L 720,620 L 720,780 L 0,780 Z"/>
      <path d="M 140,620 C 140,560 170,540 180,520 C 190,540 220,560 220,620 Z"/>
      <rect x="178" y="500" width="4" height="20" fill="url(#grad-gold)"/>
      <circle cx="180" cy="498" r="3" fill="url(#grad-gold)"/>
      <path d="M 480,620 C 480,550 515,530 525,510 C 535,530 570,550 570,620 Z"/>
      <rect x="523" y="490" width="4" height="20" fill="url(#grad-gold)"/>
      <circle cx="525" cy="488" r="3" fill="url(#grad-gold)"/>
    </g>

    <!-- Sandstone Wall & Grand Cusped Arch Opening -->
    <g id="s1-architecture">
      <path d="M 0,0 L 720,0 L 720,1280 L 0,1280 Z 
               M 70,1180 L 70,380 
               C 70,305 98,268 145,248 
               C 174,210 222,182 280,172 
               C 318,135 360,95 360,85 
               C 360,95 402,135 440,172 
               C 498,182 546,210 575,248 
               C 622,268 650,305 650,380 
               L 650,1180 Z" fill="url(#grad-sandstone)" fill-rule="evenodd"/>
      <path d="M 68,1180 L 68,380 C 68,305 96,268 143,248 C 172,210 220,182 278,172 C 316,135 360,95 360,85 C 360,95 404,135 442,172 C 500,182 548,210 577,248 C 624,268 652,305 652,380 L 652,1180" stroke="url(#grad-gold)" stroke-width="5" fill="none"/>
      <path d="M 82,1180 L 82,390 C 82,320 106,285 150,265 C 180,228 225,200 280,190 C 320,155 360,118 360,108 C 360,118 400,155 440,190 C 495,200 540,228 570,265 C 614,285 638,320 638,390 L 638,1180" stroke="#FFF7CC" stroke-width="2" stroke-dasharray="5,6" fill="none"/>

      <!-- Cascading Bougainvillea / Jasmine Creepers with Blooming Red Flowers -->
      <g>
        <path d="M 50,120 Q 120,170 160,250 T 190,380" stroke="#1B4D24" stroke-width="5" fill="none"/>
        <path d="M 670,130 Q 600,180 560,260 T 530,390" stroke="#1B4D24" stroke-width="5" fill="none"/>
        <g fill="#D91438">
          <circle cx="150" cy="230" r="8"/><circle cx="160" cy="224" r="7"/><circle cx="155" cy="238" r="6"/>
          <circle cx="185" cy="310" r="8"/><circle cx="195" cy="304" r="7"/><circle cx="190" cy="318" r="6"/>
          <circle cx="570" cy="240" r="8"/><circle cx="560" cy="234" r="7"/><circle cx="565" cy="248" r="6"/>
          <circle cx="540" cy="320" r="8"/><circle cx="530" cy="314" r="7"/><circle cx="535" cy="328" r="6"/>
        </g>
      </g>
    </g>

    <!-- Hanging Filigree Brass Lantern with Radiant Sunburst Glow -->
    <g id="s1-lantern" transform="translate(360, 240)">
      <line x1="0" y1="-160" x2="0" y2="0" stroke="url(#grad-gold)" stroke-width="3"/>
      <path d="M 0,-30 L 14,-15 L -14,-15 Z" fill="url(#grad-gold)"/>
      <path d="M -35,0 C -35,-18 35,-18 35,0 Z" fill="url(#grad-gold)"/>
      <rect x="-28" y="0" width="56" height="75" rx="6" fill="rgba(255, 230, 160, 0.28)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <circle id="s1-glow" cx="0" cy="38" r="160" fill="url(#grad-lantern-glow)" opacity="0.95"/>
      <path id="s1-flame" d="M -8,52 C -14,30 0,12 0,0 C 0,12 14,30 8,52 Z" fill="#FFE885"/>
      <path d="M -35,75 L 35,75 L 20,90 L -20,90 Z" fill="url(#grad-gold)"/>
      <circle cx="0" cy="102" r="6" fill="url(#grad-ruby)"/>
    </g>

    <!-- White Makrana Marble Balustrade with Carved Floral Jali -->
    <g transform="translate(60, 750)">
      <rect x="0" y="0" width="600" height="36" fill="url(#grad-marble)" stroke="#D4AF37" stroke-width="1.5"/>
      <rect x="0" y="36" width="600" height="150" fill="#E8E2D5"/>
      <g fill="#3B1C10" opacity="0.75">
        <circle cx="60" cy="110" r="28"/><circle cx="150" cy="110" r="28"/><circle cx="240" cy="110" r="28"/>
        <circle cx="330" cy="110" r="28"/><circle cx="420" cy="110" r="28"/><circle cx="510" cy="110" r="28"/>
      </g>
      <rect x="0" y="186" width="600" height="28" fill="url(#grad-marble)"/>
    </g>

    <!-- FULLY ILLUSTRATED PRINCE (Left, Profile in Royal Angrakha) -->
    <g id="s1-prince" transform="translate(190, 480)">
      <path d="M 0,-40 C -10,-85 60,-95 85,-65 C 98,-45 80,-20 50,-25 Z" fill="#14283D"/>
      <path d="M 25,-40 C 45,-60 75,-50 82,-35 C 75,-15 45,-15 25,-25 Z" fill="#1D3E60"/>
      <path d="M 75,-65 C 80,-95 95,-115 105,-125 C 98,-100 88,-80 82,-65 Z" fill="url(#grad-gold)"/>
      <circle cx="78" cy="-62" r="5" fill="url(#grad-emerald)"/>
      <circle cx="78" cy="-52" r="3" fill="url(#grad-pearl)"/>

      <!-- Profile Face (Anidoodle Loomis Canon) -->
      <path d="M 40,-35 C 50,-35 58,-30 62,-22 C 66,-14 62,-8 68,-2 C 74,4 82,10 80,18 C 78,22 70,24 68,28 C 65,34 68,42 62,48 C 55,54 45,56 35,58 C 22,58 10,48 5,35 Z" fill="#DE9E78"/>
      <path d="M 60,-12 Q 68,-16 75,-10" stroke="#1A0D05" stroke-width="2.5" fill="none"/>
      <path d="M 64,-6 Q 70,-10 76,-4 Q 70,0 64,-6 Z" fill="#FFFFFF"/>
      <circle cx="71" cy="-5" r="2.8" fill="#1A0D05"/>
      <circle cx="70" cy="-6" r="1" fill="#FFFFFF"/>
      <path d="M 68,26 C 74,28 80,32 76,36 C 70,36 65,32 62,30 Z" fill="#1A0D05"/>
      <path d="M 35,45 C 48,56 60,54 62,48 C 55,42 45,40 35,42 Z" fill="#1A0D05"/>

      <!-- Embroidered Ivory Angrakha Body -->
      <path d="M -40,110 C -20,60 10,60 45,58 L 75,100 C 60,180 30,240 10,270 L -60,270 Z" fill="url(#grad-prince-robe)"/>
      <path d="M 45,58 L 20,130 L 60,200" stroke="url(#grad-gold)" stroke-width="6" fill="none"/>
      <path d="M 35,70 Q 10,120 40,160" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="4,5" fill="none"/>

      <!-- Right Arm Extending holding the Rose Stem -->
      <g transform="translate(45, 120)">
        <path d="M 0,0 C 40,25 80,50 120,70 L 105,95 C 65,75 30,45 -10,15 Z" fill="url(#grad-prince-robe)"/>
        <rect x="95" y="65" width="16" height="28" rx="3" fill="url(#grad-gold)" transform="rotate(-30 95 65)"/>
        <!-- True Hand Anatomy -->
        <g transform="translate(115, 82)">
          <path d="M 0,0 C 15,-5 28,0 35,12 C 30,22 15,25 0,18 Z" fill="#DE9E78"/>
          <path d="M 12,-2 C 22,-8 32,-5 36,4 C 30,8 20,8 14,4 Z" fill="#E8B08D"/>
          <path d="M 18,5 C 28,2 38,6 40,14 C 34,18 25,16 20,12 Z" fill="#DE9E78"/>
          <circle cx="28" cy="8" r="4.5" fill="url(#grad-emerald)"/>
          <path d="M 15,16 C 24,14 32,18 34,25 C 28,28 20,26 16,22 Z" fill="#C98A66"/>
          <path d="M -2,4 C 8,2 18,8 18,16 C 10,18 2,14 -2,8 Z" fill="#E8B08D"/>
        </g>
      </g>
    </g>

    <!-- FULLY ILLUSTRATED PRINCESS (Right, Profile in Royal Lehenga & Veil) -->
    <g id="s1-princess" transform="translate(530, 480)">
      <line x1="-35" y1="-65" x2="-55" y2="-32" stroke="url(#grad-gold)" stroke-width="2"/>
      <circle cx="-55" cy="-30" r="4.5" fill="url(#grad-ruby)"/>
      <circle cx="-55" cy="-24" r="2.5" fill="url(#grad-pearl)"/>

      <path d="M -40,-35 C -50,-35 -58,-30 -62,-22 C -66,-14 -62,-8 -68,-2 C -74,4 -80,10 -78,16 C -75,20 -68,22 -66,26 C -64,32 -67,38 -62,44 C -55,50 -45,54 -35,56 C -22,56 -10,46 -5,35 Z" fill="#F5C4AC"/>
      <path d="M -60,-12 Q -68,-16 -75,-10" stroke="#1A0D05" stroke-width="2.5" fill="none"/>
      <path d="M -64,-6 Q -70,-10 -76,-4 Q -70,0 -64,-6 Z" fill="#FFFFFF"/>
      <circle cx="-71" cy="-5" r="2.8" fill="#1A0D05"/>
      <circle cx="-70" cy="-6" r="1" fill="#FFFFFF"/>
      <path d="M -76,-4 L -82,-7" stroke="#1A0D05" stroke-width="1.8"/>
      <circle cx="-76" cy="14" r="5" fill="none" stroke="url(#grad-gold)" stroke-width="1.5"/>
      <circle cx="-81" cy="18" r="2" fill="url(#grad-pearl)"/>
      <path d="M -68,26 Q -74,27 -70,30 Q -65,31 -62,28 Z" fill="#E11D48"/>

      <g transform="translate(-32, 10)">
        <circle cx="0" cy="0" r="3" fill="url(#grad-gold)"/>
        <path d="M -6,8 L 6,8 L 0,18 Z" fill="url(#grad-gold)"/>
        <circle cx="0" cy="20" r="2" fill="url(#grad-pearl)"/>
      </g>

      <!-- Billowing Sheer Emerald & Gold Odhni / Dupatta -->
      <path id="s1-p-dupatta" d="M -20,-45 C 30,-65 80,-40 130,-50 C 165,-60 200,-35 230,-45 C 200,-10 160,-20 120,-10 C 70,5 20,-15 -20,-20 Z" fill="rgba(5, 150, 105, 0.85)" stroke="url(#grad-gold)" stroke-width="2"/>

      <path d="M 40,110 C 20,60 -10,60 -45,58 L -75,100 C -60,180 -30,240 -10,270 L 60,270 Z" fill="url(#grad-princess-sleeve)"/>
      <path d="M -45,58 L -20,130 L -60,200" stroke="url(#grad-gold)" stroke-width="6" fill="none"/>

      <!-- Left Arm Extending with Henna-Adorned Hand & Gold/Red Bangles -->
      <g transform="translate(-45, 120)">
        <path d="M 0,0 C -40,25 -80,50 -120,70 L -105,95 C -65,75 -30,45 10,15 Z" fill="url(#grad-princess-sleeve)"/>
        <g transform="translate(-95, 65) rotate(30)">
          <rect x="-8" y="-14" width="4" height="28" fill="url(#grad-gold)"/>
          <rect x="-3" y="-13" width="3" height="26" fill="#C9184A"/>
          <rect x="1" y="-13" width="3" height="26" fill="#C9184A"/>
          <rect x="5" y="-14" width="4" height="28" fill="url(#grad-gold)"/>
        </g>
        <g transform="translate(-115, 82)">
          <path d="M 0,0 C -15,-5 -28,0 -35,12 C -30,22 -15,25 0,18 Z" fill="#F5C4AC"/>
          <circle cx="-16" cy="10" r="6" fill="#6B160A" opacity="0.85"/>
          <circle cx="-16" cy="10" r="2.5" fill="#F5C4AC"/>
          <path d="M -12,-2 C -22,-8 -32,-5 -36,4 C -30,8 -20,8 -14,4 Z" fill="#F5C4AC"/>
          <circle cx="-34" cy="2" r="3" fill="#6B160A"/>
          <path d="M -18,5 C -28,2 -38,6 -40,14 C -34,18 -25,16 -20,12 Z" fill="#F5C4AC"/>
          <circle cx="-28" cy="8" r="4.5" fill="url(#grad-ruby)"/>
          <circle cx="-38" cy="12" r="3" fill="#6B160A"/>
          <path d="M -15,16 C -24,14 -32,18 -34,25 C -28,28 -20,26 -16,22 Z" fill="#F5C4AC"/>
          <circle cx="-32" cy="23" r="3" fill="#6B160A"/>
          <path d="M 2,4 C -8,2 -18,8 -18,16 C -10,18 -2,14 2,8 Z" fill="#F5C4AC"/>
        </g>
      </g>
    </g>

    <!-- THE ICONIC BLOOMING RED ROSE (Held Between Their Hands in Center) -->
    <g id="s1-rose" transform="translate(360, 680)">
      <circle cx="0" cy="0" r="60" fill="url(#grad-lantern-glow)" opacity="0.75"/>
      <path d="M 0,10 Q -5,40 0,75" stroke="#1B4D24" stroke-width="4" fill="none"/>
      <path d="M 0,25 Q 18,15 25,28 Q 12,32 0,25 Z" fill="#2D6A4F"/>
      <circle cx="0" cy="0" r="28" fill="#590D22"/>
      <path d="M -22,-10 C -25,-25 0,-32 15,-25 C 28,-18 28,-2 18,10 C 5,20 -15,15 -22,-10 Z" fill="url(#grad-rose)"/>
      <path d="M -14,-18 C -10,-28 12,-28 18,-16 C 22,-5 12,10 0,12 C -12,12 -18,-5 -14,-18 Z" fill="#FF4D6D"/>
      <circle cx="0" cy="-5" r="8" fill="#FFF0F3" opacity="0.4"/>
    </g>
  </g>

  <!-- ================= SCENE 2: THE DEVOTED HEART & LOVE LETTER (4.5s - 8.8s) ================= -->
  <!-- "यह दिल तेरा दीवाना सी" -->
  <g id="scene-2" opacity="0">
    <rect width="720" height="1280" fill="#2A0B18"/>
    <!-- Intimate Golden Hour Palace Interior -->
    <circle cx="360" cy="520" r="380" fill="url(#grad-sunset-sky)" opacity="0.75"/>
    <circle cx="360" cy="520" r="240" fill="url(#grad-lantern-glow)" opacity="0.9"/>

    <!-- Prince Close-Up Torso in Royal Navy Angrakha -->
    <g transform="translate(360, 660)">
      <path d="M -240,450 L -180,60 L 0,-60 L 180,60 L 240,450 Z" fill="#14283D"/>
      <path d="M 0,-60 L -35,80 L 0,220 L 35,80 Z" stroke="url(#grad-gold)" stroke-width="8" fill="none"/>
      <path d="M 0,-60 L 0,220" stroke="#FFF3B0" stroke-width="2"/>
    </g>

    <!-- ANIDOODLE HANDS PRESSING LOVE LETTER TO THE HEART -->
    <g id="s2-heart-group" transform="translate(360, 520)">
      <!-- The Vintage Love Letter (Parchment with Red Royal Wax Seal & Gold Border) -->
      <g id="s2-letter" transform="translate(-65, -95) rotate(-8)">
        <rect x="0" y="0" width="130" height="180" rx="6" fill="url(#grad-letter)" stroke="url(#grad-gold)" stroke-width="2.5"/>
        <path d="M 8,8 L 24,8 M 8,8 L 8,24" stroke="url(#grad-gold)" stroke-width="2"/>
        <path d="M 122,8 L 106,8 M 122,8 L 122,24" stroke="url(#grad-gold)" stroke-width="2"/>
        <path d="M 8,172 L 24,172 M 8,172 L 8,156" stroke="url(#grad-gold)" stroke-width="2"/>
        <path d="M 122,172 L 106,172 M 122,172 L 122,156" stroke="url(#grad-gold)" stroke-width="2"/>
        <line x1="20" y1="36" x2="110" y2="36" stroke="#4A2810" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="20" y1="56" x2="100" y2="56" stroke="#4A2810" stroke-width="2" stroke-linecap="round"/>
        <line x1="20" y1="76" x2="105" y2="76" stroke="#4A2810" stroke-width="2" stroke-linecap="round"/>
        <line x1="20" y1="96" x2="85" y2="96" stroke="#4A2810" stroke-width="2" stroke-linecap="round"/>
        <circle cx="65" cy="138" r="20" fill="#881337"/>
        <circle cx="65" cy="138" r="16" fill="#BE123C"/>
        <path d="M 65,130 C 60,124 53,127 53,134 C 53,142 65,148 65,148 C 65,148 77,142 77,134 C 77,127 70,124 65,130 Z" fill="#FFE4E6"/>
      </g>

      <!-- Right Hand Gripping Letter -->
      <g transform="translate(45, 30)">
        <path d="M 160,250 L 50,70 L 0,90 L 100,270 Z" fill="#14283D"/>
        <rect x="35" y="65" width="16" height="30" rx="3" fill="url(#grad-gold)" transform="rotate(-25 35 65)"/>
        <path d="M 10,75 C -5,55 -25,45 -48,45 C -68,45 -85,58 -92,78 C -82,100 -55,115 -20,118 Z" fill="#DE9E78"/>
        <path d="M -30,50 C -25,25 -20,0 -8,-15 C -2,-18 5,-14 2,-6 C -6,12 -12,35 -18,55 Z" fill="#E8B08D"/>
        <path d="M -52,52 C -48,24 -42,-4 -32,-20 C -26,-23 -20,-19 -22,-11 C -30,10 -36,34 -40,60 Z" fill="#DE9E78"/>
        <path d="M -72,62 C -68,36 -62,12 -52,-5 C -46,-8 -42,-5 -44,2 C -52,20 -58,42 -62,68 Z" fill="#C98A66"/>
        <rect x="-65" y="18" width="14" height="6" rx="2" fill="url(#grad-gold)" transform="rotate(18 -65 18)"/>
        <circle cx="-58" cy="21" r="3.5" fill="url(#grad-emerald)"/>
        <path d="M -85,76 C -82,56 -78,38 -72,22 C -67,19 -64,22 -66,28 C -70,44 -74,62 -76,82 Z" fill="#B87B5E"/>
        <path d="M 5,85 C -8,78 -25,75 -42,80 C -50,82 -52,88 -46,92 C -30,98 -12,100 2,102 Z" fill="#E8B08D"/>
      </g>

      <!-- Left Hand Resting Flat Over Heart -->
      <g transform="translate(-140, 60)">
        <path d="M -140,220 L -40,70 L 5,90 L -80,240 Z" fill="#14283D"/>
        <rect x="-45" y="70" width="16" height="28" rx="3" fill="url(#grad-gold)" transform="rotate(25 -45 70)"/>
        <path d="M -5,75 C 15,55 35,45 60,45 C 80,45 95,58 105,75 C 95,98 70,112 35,115 Z" fill="#DE9E78"/>
        <path d="M 55,48 C 70,32 88,20 108,15 C 114,17 115,22 110,26 C 92,34 78,45 65,60 Z" fill="#E8B08D"/>
        <path d="M 75,52 C 92,38 112,28 132,25 C 137,27 138,32 133,36 C 115,44 100,55 86,70 Z" fill="#DE9E78"/>
        <path d="M 92,65 C 108,52 126,45 144,44 C 149,46 150,51 145,55 C 128,62 115,72 102,85 Z" fill="#C98A66"/>
      </g>
    </g>
  </g>

  <!-- ================= SCENE 3: COLD MIDNIGHT RAIN & SCATTERED PETALS (8.8s - 13.5s) ================= -->
  <!-- "मेरा यह हाल होना सी" -->
  <g id="scene-3" opacity="0">
    <rect width="720" height="1280" fill="url(#grad-night-sky)"/>
    
    <!-- Grand Palace Architecture Bathed in Cool Moonlight -->
    <g id="s3-architecture">
      <path d="M 0,0 L 720,0 L 720,1280 L 0,1280 Z 
               M 70,1180 L 70,380 
               C 70,305 98,268 145,248 
               C 174,210 222,182 280,172 
               C 318,135 360,95 360,85 
               C 360,95 402,135 440,172 
               C 498,182 546,210 575,248 
               C 622,268 650,305 650,380 
               L 650,1180 Z" fill="url(#grad-night-stone)" fill-rule="evenodd"/>
      <path d="M 68,1180 L 68,380 C 68,305 96,268 143,248 C 172,210 220,182 278,172 C 316,135 360,95 360,85 C 360,95 404,135 442,172 C 500,182 548,210 577,248 C 624,268 652,305 652,380 L 652,1180" stroke="#4A7599" stroke-width="4.5" fill="none"/>
      <path d="M 82,1180 L 82,390 C 82,320 106,285 150,265 C 180,228 225,200 280,190 C 320,155 360,118 360,108 C 360,118 400,155 440,190 C 495,200 540,228 570,265 C 614,285 638,320 638,390 L 638,1180" stroke="#90CAF9" stroke-width="1.8" stroke-dasharray="4,6" fill="none" opacity="0.65"/>
    </g>

    <!-- Wet Marble Window Sill with Glistening Reflections -->
    <g transform="translate(60, 750)">
      <rect x="0" y="0" width="600" height="36" fill="#1C3852" stroke="#4A7599" stroke-width="1.5"/>
      <rect x="15" y="4" width="570" height="10" rx="3" fill="#B0D8F8" opacity="0.45"/>
      <rect x="0" y="36" width="600" height="150" fill="#122538"/>
      
      <!-- SCATTERED WILTED RED ROSE PETALS (Heartbreak) -->
      <g fill="#A81528">
        <path d="M 80,15 C 95,5 115,12 110,24 C 98,28 85,24 80,15 Z"/>
        <path d="M 160,18 C 175,8 192,15 185,26 C 175,30 165,26 160,18 Z"/>
        <path d="M 280,12 C 295,4 312,10 305,22 C 295,26 285,22 280,12 Z"/>
        <path d="M 420,20 C 438,10 455,18 448,30 C 438,34 425,30 420,20 Z"/>
        <path d="M 510,14 C 525,6 542,12 536,24 C 526,28 515,24 510,14 Z"/>
      </g>
    </g>

    <!-- Solitary Prince Sitting in Grief by the Window -->
    <g id="s3-prince-grief" transform="translate(240, 520)">
      <!-- Head Bowed with Moonlit Edge Highlight -->
      <path d="M -10,-20 C -20,-65 40,-75 65,-45 C 75,-25 60,-5 35,-10 Z" fill="#10253B"/>
      <path d="M 25,-48 C 45,-68 65,-58 70,-42" stroke="#90CAF9" stroke-width="2" fill="none"/>
      <path d="M 20,-15 C 32,-15 42,-8 45,0 C 48,10 42,20 38,28 C 30,36 18,38 8,36 Z" fill="#B88A70"/>
      <!-- Torso in Melancholy -->
      <path d="M -50,90 C -30,40 5,40 35,38 L 55,80 C 40,160 20,220 5,250 L -60,250 Z" fill="#0E2034"/>
      <!-- Hand Resting Beside Scattered Petals -->
      <g transform="translate(35, 100)">
        <path d="M 0,0 C 35,20 70,40 100,60 L 85,82 C 55,65 25,40 -10,15 Z" fill="#0E2034"/>
        <path d="M 95,70 C 110,65 125,72 135,82 C 128,92 115,95 98,90 Z" fill="#B88A70"/>
        <circle id="s3-drop" cx="138" cy="98" r="3" fill="#B0D8F8" opacity="0.9"/>
      </g>
    </g>

    <!-- ANTIQUE BRASS POCKET WATCH (Ticking from 11:30 to 4:00 AM) -->
    <g id="s3-watch" transform="translate(490, 715)">
      <circle cx="0" cy="0" r="46" fill="url(#grad-gold)" stroke="#5A400C" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="38" fill="#F8F9FA"/>
      <text x="0" y="-24" font-size="11" font-weight="700" text-anchor="middle" fill="#1A1A1A">XII</text>
      <text x="28" y="4" font-size="10" font-weight="700" text-anchor="middle" fill="#1A1A1A">III</text>
      <text x="0" y="32" font-size="10" font-weight="700" text-anchor="middle" fill="#1A1A1A">VI</text>
      <text x="-28" y="4" font-size="10" font-weight="700" text-anchor="middle" fill="#1A1A1A">IX</text>
      <line id="s3-hour-hand" x1="0" y1="0" x2="0" y2="-18" stroke="#1A1A1A" stroke-width="3.5" stroke-linecap="round"/>
      <line id="s3-min-hand" x1="0" y1="0" x2="0" y2="-26" stroke="#D32F2F" stroke-width="2" stroke-linecap="round"/>
      <circle cx="0" cy="0" r="4" fill="url(#grad-gold)"/>
    </g>

    <!-- Extinguished Diya with Rising Smoke Wisp -->
    <g transform="translate(180, 720)">
      <path d="M -25,25 Q 0,40 25,25 Q 20,10 0,12 Q -20,10 -25,25 Z" fill="url(#grad-gold)"/>
      <circle cx="0" cy="18" r="4.5" fill="#FF3300"/>
      <path id="s3-smoke" d="M 0,15 Q 15,-20 -10,-60 T 12,-110 T -15,-170" stroke="rgba(215, 235, 255, 0.7)" stroke-width="5" fill="none" stroke-linecap="round"/>
    </g>
  </g>

  <!-- ================= SCENE 4: CRESCENT MOON, LOTUS POND & HOURGLASS OF FATE (13.5s - 18.17s) ================= -->
  <!-- "तेरा मिलना बहाना सी..." -->
  <g id="scene-4" opacity="0">
    <rect width="720" height="1280" fill="url(#grad-night-sky)"/>
    
    <!-- Grand Palace Architecture Framing the Moonlit Night -->
    <g id="s4-architecture">
      <path d="M 0,0 L 720,0 L 720,1280 L 0,1280 Z 
               M 70,1180 L 70,380 
               C 70,305 98,268 145,248 
               C 174,210 222,182 280,172 
               C 318,135 360,95 360,85 
               C 360,95 402,135 440,172 
               C 498,182 546,210 575,248 
               C 622,268 650,305 650,380 
               L 650,1180 Z" fill="url(#grad-night-stone)" fill-rule="evenodd"/>
      <path d="M 68,1180 L 68,380 C 68,305 96,268 143,248 C 172,210 220,182 278,172 C 316,135 360,95 360,85 C 360,95 404,135 442,172 C 500,182 548,210 577,248 C 624,268 652,305 652,380 L 652,1180" stroke="#4A7599" stroke-width="5" fill="none"/>
    </g>

    <!-- Luminous Chandramukhi Crescent Moon with Radiating Lunar Halo -->
    <circle cx="360" cy="270" r="260" fill="url(#grad-moon-glow)" opacity="0.9"/>
    <g transform="translate(360, 270)">
      <path d="M -35,-70 
               A 80,80 0 1,0 70,35 
               A 70,70 0 1,1 -35,-70 Z" fill="#F0F8FF"/>
      <circle cx="20" cy="-25" r="9" fill="#D4E6F7" opacity="0.55"/>
      <circle cx="38" cy="2" r="14" fill="#D4E6F7" opacity="0.55"/>
      <circle cx="-5" cy="32" r="11" fill="#D4E6F7" opacity="0.55"/>
    </g>

    <!-- Sparkling Star Clusters in Clear Night Sky -->
    <g fill="#FFFFFF" opacity="0.9">
      <circle cx="140" cy="160" r="2.2"/><circle cx="200" cy="220" r="1.6"/><circle cx="250" cy="130" r="2.5"/>
      <circle cx="520" cy="150" r="2.2"/><circle cx="590" cy="230" r="1.8"/><circle cx="470" cy="110" r="1.6"/>
      <circle cx="160" cy="360" r="1.8"/><circle cx="560" cy="370" r="2.2"/>
    </g>

    <!-- Moonlit Reflecting Pond with Water Ripples & Lotus -->
    <g transform="translate(60, 750)">
      <rect x="0" y="0" width="600" height="36" fill="#1C3852" stroke="#4A7599" stroke-width="1.5"/>
      <rect x="15" y="4" width="570" height="10" rx="3" fill="#B0D8F8" opacity="0.45"/>
      <rect x="0" y="36" width="600" height="150" fill="#0D2033"/>
      <!-- Soft Lunar Reflection Ripples in Pond -->
      <ellipse cx="300" cy="90" rx="140" ry="14" fill="none" stroke="#6BA4CC" stroke-width="1.8" opacity="0.6"/>
      <ellipse cx="300" cy="115" rx="90" ry="9" fill="none" stroke="#6BA4CC" stroke-width="1.5" opacity="0.5"/>
      <!-- Lotus Flower in Pond -->
      <g transform="translate(180, 85)">
        <path d="M 0,-15 C 8,-30 22,-20 18,-5 C 10,5 -5,5 -18,-5 C -22,-20 -8,-30 0,-15 Z" fill="#FDA4AF"/>
        <path d="M 0,-20 C 5,-32 15,-25 10,-8 C 5,2 -5,2 -10,-8 C -15,-25 -5,-32 0,-20 Z" fill="#F43F5E"/>
        <circle cx="0" cy="-6" r="3" fill="#FFE885"/>
      </g>
    </g>

    <!-- MONUMENTAL BRASS HOURGLASS OF FATE (Destiny Sand Trickling) -->
    <g id="s4-hourglass" transform="translate(360, 660)">
      <path d="M -90,130 L 90,130 L 70,110 L -70,110 Z" fill="url(#grad-gold)"/>
      <path d="M -90,-130 L 90,-130 L 70,-110 L -70,-110 Z" fill="url(#grad-gold)"/>
      <line x1="-75" y1="-110" x2="-75" y2="110" stroke="url(#grad-gold)" stroke-width="6"/>
      <line x1="75" y1="-110" x2="75" y2="110" stroke="url(#grad-gold)" stroke-width="6"/>

      <!-- Hourglass Blown Glass Chambers -->
      <path d="M -60,-110 L 60,-110 
               C 50,-50 15,-15 10,0 
               C 15,15 50,50 60,110 
               L -60,110 
               C -50,50 -15,15 -10,0 
               C -15,-15 -50,-50 -60,-110 Z" fill="rgba(225, 242, 255, 0.22)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      
      <!-- Upper Bulb Crimson Sand Level (Draining Downwards) -->
      <path id="s4-sand-top" d="M -45,-40 Q 0,-30 45,-40 L 10,0 L -10,0 Z" fill="#9B111E"/>
      <line x1="0" y1="0" x2="0" y2="90" stroke="#FF4D6D" stroke-width="3" stroke-dasharray="3,3"/>
      <path id="s4-sand-bot" d="M -48,105 Q 0,70 48,105 Z" fill="#590D22"/>
    </g>

    <!-- Drifting Lone Red Rose Petal Floating Downwards -->
    <g id="s4-petal" transform="translate(360, 440)">
      <path d="M 0,0 C 22,-12 38,6 30,24 C 18,30 0,22 0,0 Z" fill="url(#grad-rose)"/>
    </g>

    <!-- Grand Final Calligraphic Monument Seal -->
    <g id="s4-seal" transform="translate(360, 960)">
      <line x1="-180" y1="-45" x2="180" y2="-45" stroke="url(#grad-gold)" stroke-width="2"/>
      <text y="-10" fill="#FFE885" font-size="38" font-weight="700" text-anchor="middle" letter-spacing="4px">
        मोहब्बत सी, ज़माना सी
      </text>
      <text y="28" fill="#E2BA60" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="5px">
        MOHABBAT SI ZAMANA SI // THE DESTINY
      </text>
      <line x1="-180" y1="50" x2="180" y2="50" stroke="url(#grad-gold)" stroke-width="2"/>
    </g>
  </g>

  <!-- ================= MASTER SUBTITLE CARDS (0.0s - 18.17s) ================= -->
  <g id="subtitles">
    <!-- Subtitle 1 (0.2s - 4.4s) -->
    <g id="sub-1" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(18, 4, 12, 0.94)" stroke="url(#grad-gold)" stroke-width="2.5"/>
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
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(18, 4, 12, 0.94)" stroke="url(#grad-gold)" stroke-width="2.5"/>
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
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(8, 16, 28, 0.95)" stroke="#90CAF9" stroke-width="2.5"/>
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
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(14, 6, 12, 0.95)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        तेरा मिलना बहाना सी...
      </text>
      <text x="250" y="90" fill="#FFE082" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        TERA MILNA BAHANA SI
      </text>
      <text x="250" y="118" fill="#CFA138" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // MEETING YOU WAS BUT DESTINY'S PRETEXT
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

// 1. Handmade Cotton Rag Paper Texture
function initPaperTexture() {
  const pCan = document.getElementById('paper-canvas');
  const pCtx = pCan.getContext('2d');
  const imgData = pCtx.createImageData(720, 1280);
  const data = imgData.data;

  for (let i = 0; i < data.length; i += 4) {
    const n = Math.random();
    const val = Math.floor(220 + n * 35);
    data[i] = val;
    data[i+1] = Math.floor(val * 0.96);
    data[i+2] = Math.floor(val * 0.88);
    data[i+3] = 255;
  }
  pCtx.putImageData(imgData, 0, 0);
}

// 2. Dynamic Atmosphere FX (Sunset Dust Motes, Diagonal Rain, Floating Petals)
function drawFX(t) {
  ctx.clearRect(0, 0, 720, 1280);

  if (t < 8.8) {
    // Act 1 & 2: Golden Sunset Dust Motes
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
    const numRain = 90;
    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'rgba(165, 215, 250, 0.45)';
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
    // Act 4: Drifting Rose Petals & Sparkling Lunar Rays
    const numPetals = 18;
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
      ctx.fillStyle = 'rgba(201, 24, 74, 0.7)';
      ctx.fill();
      ctx.restore();
    }
  }
}

// 3. Main Render Loop
function render(t) {
  t = Math.max(0, Math.min(t, DUR));

  const s1 = document.getElementById('scene-1');
  const s2 = document.getElementById('scene-2');
  const s3 = document.getElementById('scene-3');
  const s4 = document.getElementById('scene-4');

  const sub1 = document.getElementById('sub-1');
  const sub2 = document.getElementById('sub-2');
  const sub3 = document.getElementById('sub-3');
  const sub4 = document.getElementById('sub-4');

  // Scene Visibility & Smooth Crossfades
  if (t < 4.5) {
    // Scene 1: Sunset Balcony Lovers & Rose (0.0s - 4.5s)
    s1.style.display = 'inline';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Lantern gentle sway & organic flame flicker
    const lGlow = document.getElementById('s1-glow');
    const lFlame = document.getElementById('s1-flame');
    const sway = Math.sin(t * 2.2) * 3.5;
    const flick = 1 + 0.08 * Math.sin(t * 24) + 0.04 * Math.cos(t * 39);
    document.getElementById('s1-lantern').setAttribute('transform', `translate(360, 240) rotate(${sway.toFixed(1)} 0 -160)`);
    lFlame.setAttribute('transform', `scale(${flick.toFixed(3)})`);
    lGlow.setAttribute('r', (160 * flick).toFixed(1));

    // Princess Odhni fluttering softly in the evening breeze
    const dup = document.getElementById('s1-p-dupatta');
    const dWave = Math.sin(t * 3.8) * 8;
    dup.setAttribute('d', `M -20,-45 C 30,${-65 + dWave} 80,${-40 - dWave} 130,${-50 + dWave} C 165,-60 200,-35 230,-45 C 200,-10 160,-20 120,-10 C 70,5 20,-15 -20,-20 Z`);

    // Rose pulse in center
    const rPulse = 1 + 0.03 * Math.sin(t * 3);
    document.getElementById('s1-rose').setAttribute('transform', `translate(360, 680) scale(${rPulse.toFixed(3)})`);

    // Smooth Dissolve into Scene 2
    if (t > 4.1) {
      const outP = (t - 4.1) / 0.4;
      s1.setAttribute('opacity', (1 - outP).toFixed(2));
    } else {
      s1.setAttribute('opacity', '1');
    }
  } else if (t < 8.8) {
    // Scene 2: The Devoted Heart & Love Letter (4.5s - 8.8s)
    s1.style.display = 'none';
    s2.style.display = 'inline';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Heartbeat pulse of the letter and hands
    const beat = 1 + 0.04 * Math.sin(t * 6.2);
    document.getElementById('s2-heart-group').setAttribute('transform', `translate(360, 520) scale(${beat.toFixed(3)})`);

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
    // Scene 3: Cold Midnight Rain, Solitude & Clock (8.8s - 13.5s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'inline';
    s4.style.display = 'none';

    // Pocket Watch Hands Ticking from 11:30 to 4:00 AM
    const watchHour = document.getElementById('s3-hour-hand');
    const watchMin = document.getElementById('s3-min-hand');
    const wProg = (t - 8.8) / (13.5 - 8.8);
    const hDeg = 345 + wProg * 135;
    const mDeg = (wProg * 4.5 * 360) % 360;
    watchHour.setAttribute('transform', `rotate(${hDeg.toFixed(1)})`);
    watchMin.setAttribute('transform', `rotate(${mDeg.toFixed(1)})`);

    // Raindrop drip animation
    const drop = document.getElementById('s3-drop');
    const dropP = ((t - 8.8) * 3) % 1;
    drop.setAttribute('cy', (98 + dropP * 48).toFixed(1));
    drop.setAttribute('opacity', (1 - dropP).toFixed(2));

    // Smoke curling from extinguished diya
    const sm = document.getElementById('s3-smoke');
    const curl = Math.sin(t * 3.5) * 12;
    sm.setAttribute('d', `M 0,15 Q ${15 + curl},-20 ${-10 - curl},-60 T ${12 + curl},-110 T ${-15 - curl},-170`);

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
    // Scene 4: Crescent Moon & Hourglass of Fate (13.5s - 18.17s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'inline';

    // Hourglass Sand Draining Downwards
    const sandP = (t - 13.5) / (18.17 - 13.5);
    const topY = -40 + sandP * 30;
    const botY = 105 - sandP * 32;
    document.getElementById('s4-sand-top').setAttribute('d', `M -45,${topY.toFixed(1)} Q 0,${(topY + 10).toFixed(1)} 45,${topY.toFixed(1)} L 10,0 L -10,0 Z`);
    document.getElementById('s4-sand-bot').setAttribute('d', `M -48,105 Q 0,${botY.toFixed(1)} 48,105 Z`);

    // Drifting Rose Petal across the moon
    const petY = 320 + sandP * 360;
    const petX = 360 + Math.sin(t * 2) * 85;
    const petRot = t * 50;
    document.getElementById('s4-petal').setAttribute('transform', `translate(${petX.toFixed(1)}, ${petY.toFixed(1)}) rotate(${petRot.toFixed(1)})`);

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

// 5. Initialization
async function init() {
  initPaperTexture();

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

print('Updated index.html with architectural continuity! Length:', len(html_code))
