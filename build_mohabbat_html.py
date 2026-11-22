import os

html_content = '''<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<title>Mohabbat Si Zamana Si — Mughal Miniature Storybook (Anidoodle Craft)</title>
<link rel="stylesheet" href="fonts.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    width: 720px;
    height: 1280px;
    overflow: hidden;
    background: #080308;
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
    opacity: 0.22;
  }
  #fx-canvas {
    mix-blend-mode: screen;
  }
</style>
</head>
<body>

<svg id="stage" viewBox="0 0 720 1280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Mughal Jharokha Cusped Arch Clip -->
    <clipPath id="arch-jharokha">
      <path d="M 60,1180 L 60,380 
               C 60,300 90,260 140,240 
               C 170,200 220,170 280,160 
               C 320,120 360,80 360,70 
               C 360,80 400,120 440,160 
               C 500,170 550,200 580,240 
               C 630,260 660,300 660,380 
               L 660,1180 Z"/>
    </clipPath>

    <!-- Sunset Sky Gradient (Act 1 & 2) -->
    <linearGradient id="grad-sunset" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A0512"/>
      <stop offset="30%" stop-color="#3B0B1E"/>
      <stop offset="60%" stop-color="#7A1828"/>
      <stop offset="85%" stop-color="#D95C28"/>
      <stop offset="100%" stop-color="#FDB44B"/>
    </linearGradient>

    <!-- Stormy Night Sky Gradient (Act 3 & 4) -->
    <linearGradient id="grad-night" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#040810"/>
      <stop offset="35%" stop-color="#081424"/>
      <stop offset="70%" stop-color="#0F243A"/>
      <stop offset="100%" stop-color="#1B3852"/>
    </linearGradient>

    <!-- Antique Gold Shading -->
    <linearGradient id="grad-gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6B4F10"/>
      <stop offset="25%" stop-color="#B88A28"/>
      <stop offset="50%" stop-color="#FFE885"/>
      <stop offset="75%" stop-color="#B88A28"/>
      <stop offset="100%" stop-color="#4E3708"/>
    </linearGradient>

    <!-- Warm Lantern Radial Glow -->
    <radialGradient id="grad-lantern-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFAD0" stop-opacity="1"/>
      <stop offset="25%" stop-color="#FFA826" stop-opacity="0.85"/>
      <stop offset="65%" stop-color="#D84315" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="#D84315" stop-opacity="0"/>
    </radialGradient>

    <!-- Mystic Moon Halo -->
    <radialGradient id="grad-moon-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.95"/>
      <stop offset="35%" stop-color="#CFE7F7" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#0E2338" stop-opacity="0"/>
    </radialGradient>

    <!-- Royal Silk Angrakha Sleeves -->
    <linearGradient id="grad-lover-sleeve" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10253B"/>
      <stop offset="50%" stop-color="#1D4063"/>
      <stop offset="100%" stop-color="#0A1827"/>
    </linearGradient>

    <linearGradient id="grad-beloved-sleeve" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F091A"/>
      <stop offset="50%" stop-color="#85162E"/>
      <stop offset="100%" stop-color="#34030E"/>
    </linearGradient>

    <!-- Jewels -->
    <radialGradient id="grad-emerald" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#34D399"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#064E3B"/>
    </radialGradient>

    <radialGradient id="grad-ruby" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FB7185"/>
      <stop offset="50%" stop-color="#E11D48"/>
      <stop offset="100%" stop-color="#881337"/>
    </radialGradient>

    <radialGradient id="grad-pearl" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="70%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#94A3B8"/>
    </radialGradient>

    <!-- Vintage Love Letter Parchment -->
    <linearGradient id="grad-parchment" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="60%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#E5D3A1"/>
    </linearGradient>
  </defs>

  <!-- ================= SCENE 1: SUNSET JHAROKHA WITH LOVERS (0.0s - 4.5s) ================= -->
  <!-- "मोहब्बत सी, ज़माना सी" -->
  <g id="scene-1" opacity="1">
    <!-- Sky & Distant Horizon -->
    <rect width="720" height="1280" fill="url(#grad-sunset)"/>
    
    <!-- Distant Mountain Ridge & Mughal Domes -->
    <path d="M 0,720 Q 180,680 360,710 T 720,690 L 720,820 L 0,820 Z" fill="#2E0A1A" opacity="0.75"/>
    <path d="M 120,700 Q 140,660 160,700 Z M 520,695 Q 545,650 570,695 Z" fill="#200612"/>

    <!-- Arch Jharokha Window Frame -->
    <g id="s1-jharokha-frame">
      <!-- Wall Surrounding Arch -->
      <path d="M 0,0 L 720,0 L 720,1280 L 0,1280 Z 
               M 70,1180 L 70,380 
               C 70,305 98,268 145,248 
               C 174,210 222,182 280,172 
               C 318,135 360,95 360,85 
               C 360,95 402,135 440,172 
               C 498,182 546,210 575,248 
               C 622,268 650,305 650,380 
               L 650,1180 Z" fill="#1C0612" fill-rule="evenodd"/>
      <!-- Sandstone Arch Border Moldings -->
      <path d="M 68,1180 L 68,380 
               C 68,305 96,268 143,248 
               C 172,210 220,182 278,172 
               C 316,135 360,95 360,85 
               C 360,95 404,135 442,172 
               C 500,182 548,210 577,248 
               C 624,268 652,305 652,380 
               L 652,1180" stroke="url(#grad-gold)" stroke-width="4" fill="none"/>
      <!-- Inlaid Pearl Bead Border -->
      <path d="M 80,1180 L 80,390 C 80,320 105,285 150,265 C 180,228 225,200 280,190 C 320,155 360,118 360,108 C 360,118 400,155 440,190 C 495,200 540,228 570,265 C 615,285 640,320 640,390 L 640,1180" stroke="#FFE885" stroke-width="1.5" stroke-dasharray="4,6" fill="none" opacity="0.65"/>
    </g>

    <!-- Flowering Crimson Bougainvillea Vines cascading over the arch -->
    <g id="s1-vines">
      <path d="M 50,150 Q 120,180 180,260 T 210,380" stroke="#122B14" stroke-width="4.5" fill="none"/>
      <path d="M 670,160 Q 600,200 550,280 T 520,400" stroke="#122B14" stroke-width="4.5" fill="none"/>
      <!-- Vine Leaves -->
      <ellipse cx="140" cy="210" rx="8" ry="4.5" fill="#1B4D24" transform="rotate(25 140 210)"/>
      <ellipse cx="190" cy="290" rx="8" ry="4.5" fill="#225E2D" transform="rotate(-35 190 290)"/>
      <ellipse cx="580" cy="220" rx="8" ry="4.5" fill="#1B4D24" transform="rotate(-25 580 220)"/>
      <ellipse cx="540" cy="310" rx="8" ry="4.5" fill="#225E2D" transform="rotate(35 540 310)"/>
      <!-- Crimson Bougainvillea Blossom Clusters -->
      <g fill="#C41E3A">
        <circle cx="170" cy="245" r="7"/><circle cx="180" cy="240" r="6"/><circle cx="175" cy="252" r="5.5"/>
        <circle cx="205" cy="320" r="6.5"/><circle cx="214" cy="315" r="5.5"/><circle cx="208" cy="328" r="6"/>
        <circle cx="560" cy="255" r="7"/><circle cx="550" cy="250" r="6"/><circle cx="555" cy="262" r="5.5"/>
        <circle cx="530" cy="340" r="6.5"/><circle cx="522" cy="335" r="5.5"/><circle cx="526" cy="348" r="6"/>
      </g>
    </g>

    <!-- Central Hanging Mughal Brass Lantern -->
    <g id="s1-lantern" transform="translate(360, 260)">
      <!-- Suspension Chain -->
      <line x1="0" y1="-180" x2="0" y2="0" stroke="url(#grad-gold)" stroke-width="2.5"/>
      <!-- Lantern Dome & Finial -->
      <path d="M 0,-25 L 12,-12 L -12,-12 Z" fill="url(#grad-gold)"/>
      <path d="M -30,0 C -30,-15 30,-15 30,0 Z" fill="url(#grad-gold)"/>
      <!-- Glass Chamber with Warm Glowing Flame -->
      <rect x="-24" y="0" width="48" height="65" rx="5" fill="rgba(255, 235, 175, 0.22)" stroke="url(#grad-gold)" stroke-width="2"/>
      <!-- Radial Golden Glow Burst -->
      <circle id="s1-lantern-glow" cx="0" cy="32" r="140" fill="url(#grad-lantern-glow)" opacity="0.9"/>
      <!-- Animated Flame Core -->
      <path id="s1-lantern-flame" d="M -6,45 C -12,25 0,10 0,0 C 0,10 12,25 6,45 Z" fill="#FFE885"/>
      <!-- Base & Droplet Pendant -->
      <path d="M -30,65 L 30,65 L 18,80 L -18,80 Z" fill="url(#grad-gold)"/>
      <circle cx="0" cy="92" r="5.5" fill="url(#grad-ruby)"/>
    </g>

    <!-- Carved Marble Jali Balustrade (Terrace Sill) -->
    <g transform="translate(60, 780)">
      <rect x="0" y="0" width="600" height="35" fill="url(#grad-gold)"/>
      <rect x="0" y="35" width="600" height="150" fill="#220614"/>
      <!-- Mughal Floral Hexagonal Screen Openings -->
      <g fill="#12020A" opacity="0.85">
        <circle cx="60" cy="110" r="28"/><circle cx="150" cy="110" r="28"/><circle cx="240" cy="110" r="28"/>
        <circle cx="330" cy="110" r="28"/><circle cx="420" cy="110" r="28"/><circle cx="510" cy="110" r="28"/>
      </g>
      <rect x="0" y="185" width="600" height="25" fill="#17030D"/>
    </g>

    <!-- TWO LOVERS IN TENDER SILHOUETTE PROFILE (Anidoodle Proportioned) -->
    <!-- The Beloved (Woman, on Right Balcony) -->
    <g id="s1-beloved" transform="translate(480, 560)">
      <!-- Graceful Neck & Classical Head Profile (Loomis 3/4) -->
      <path d="M -15,80 C -10,40 -20,10 -30,-20 C -25,-40 -10,-55 10,-60 C 35,-65 55,-45 50,-15 C 45,15 30,55 35,80 Z" fill="#2E0818"/>
      <!-- Soft bun hair with Jasmine Gajra flowers -->
      <circle cx="42" cy="-25" r="22" fill="#15020B"/>
      <circle cx="45" cy="-38" r="4" fill="#FFFFFF"/><circle cx="55" cy="-30" r="4" fill="#FFFFFF"/><circle cx="58" cy="-18" r="4" fill="#FFFFFF"/><circle cx="52" cy="-8" r="4" fill="#FFFFFF"/>
      <!-- Golden Jhumka Earring -->
      <g transform="translate(15, -10)">
        <circle cx="0" cy="0" r="2.5" fill="url(#grad-gold)"/>
        <path d="M -5,6 L 5,6 L 0,14 Z" fill="url(#grad-gold)"/>
      </g>
      <!-- Flowing Silk Odhni / Dupatta caught in the evening breeze -->
      <path id="s1-dupatta" d="M 0,-15 C 30,-25 70,-10 110,-18 C 145,-25 180,-10 210,-20 C 185,15 150,5 110,12 C 70,20 30,10 0,25 Z" fill="rgba(196, 30, 58, 0.85)"/>
      <!-- Arm with red and gold bangles resting gracefully on marble sill -->
      <path d="M -5,80 C 10,120 25,170 15,220 L -35,220 C -20,175 -25,120 -35,80 Z" fill="url(#grad-beloved-sleeve)"/>
      <!-- Stacked Bangles -->
      <rect x="-10" y="195" width="30" height="4" fill="url(#grad-gold)"/>
      <rect x="-8" y="201" width="26" height="3" fill="#C41E3A"/>
      <rect x="-6" y="206" width="22" height="4" fill="url(#grad-gold)"/>
      <!-- Delicate Hand on Sill -->
      <path d="M 12,220 C 25,230 40,240 55,245 C 50,250 35,250 20,245 C 5,240 -8,230 -15,225 Z" fill="#DE9C80"/>
    </g>

    <!-- The Lover (Man, on Left Balcony, reaching softly) -->
    <g id="s1-lover" transform="translate(240, 560)">
      <!-- Broad masculine shoulders, royal turban silhouette -->
      <path d="M -60,90 C -45,30 -30,-10 -15,-40 C 5,-50 35,-50 50,-35 C 60,-10 50,30 65,90 Z" fill="#14020C"/>
      <!-- Mughal Royal Pagri Turban with Sarpech Jewel -->
      <path d="M -30,-40 C -35,-75 25,-85 45,-60 C 55,-40 40,-25 20,-35 Z" fill="#1C0612"/>
      <path d="M 35,-65 L 42,-80 L 45,-60 Z" fill="url(#grad-gold)"/>
      <circle cx="40" cy="-62" r="3" fill="url(#grad-emerald)"/>
      <!-- Arm extending towards her along the balustrade -->
      <path d="M 40,85 C 65,125 90,165 130,205 L 105,235 C 65,195 40,145 15,95 Z" fill="url(#grad-lover-sleeve)"/>
      <!-- Gold Cuff & Signet Ring -->
      <rect x="100" y="205" width="28" height="6" rx="2" fill="url(#grad-gold)" transform="rotate(-38 100 205)"/>
      <!-- Hand reaching tenderly -->
      <path d="M 125,215 C 145,225 165,232 185,235 C 180,242 165,245 145,242 C 130,238 115,230 108,222 Z" fill="#C68E6F"/>
    </g>
  </g>

  <!-- ================= SCENE 2: THE DEVOTED HEART (4.5s - 8.8s) ================= -->
  <!-- "यह दिल तेरा दीवाना सी" -->
  <g id="scene-2" opacity="0">
    <rect width="720" height="1280" fill="#1A0410"/>
    <!-- Intimate Golden Amber Halo radiating from chest -->
    <circle cx="360" cy="560" r="380" fill="url(#grad-sunset)" opacity="0.65"/>
    <circle cx="360" cy="560" r="220" fill="url(#grad-lantern-glow)" opacity="0.85"/>

    <!-- Lover's Torso & Embroidered Royal Angrakha (Navy & Gold Zari) -->
    <g transform="translate(360, 680)">
      <!-- Main Chest & Tunic drape -->
      <path d="M -220,400 L -160,50 L 0,-60 L 160,50 L 220,400 Z" fill="url(#grad-lover-sleeve)"/>
      <!-- Zardozi Gold Neckline Border -->
      <path d="M 0,-60 L -30,80 L 0,220 L 30,80 Z" stroke="url(#grad-gold)" stroke-width="8" fill="none"/>
      <path d="M 0,-60 L 0,220" stroke="#FFE885" stroke-width="2"/>
      <!-- Gold Floral Brocade Motifs -->
      <circle cx="-70" cy="120" r="6" fill="url(#grad-gold)"/><circle cx="70" cy="120" r="6" fill="url(#grad-gold)"/>
      <circle cx="-90" cy="220" r="6" fill="url(#grad-gold)"/><circle cx="90" cy="220" r="6" fill="url(#grad-gold)"/>
    </g>

    <!-- RIGHT HAND (Holding the Folded Love Letter close to the heart) -->
    <!-- True Anidoodle Anatomy: Knuckle arc, 14 phalanges, opposed thumb -->
    <g id="s2-hand-letter" transform="translate(360, 520)">
      <!-- Folded Love Letter (Vintage Parchment with Red Wax Royal Seal) -->
      <g id="s2-letter" transform="translate(-45, -70) rotate(-12)">
        <rect x="0" y="0" width="110" height="150" rx="4" fill="url(#grad-parchment)" stroke="#B88A28" stroke-width="1.5"/>
        <!-- Calligraphic Ink Lines -->
        <line x1="15" y1="28" x2="95" y2="28" stroke="#542B08" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
        <line x1="15" y1="45" x2="85" y2="45" stroke="#542B08" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <line x1="15" y1="62" x2="90" y2="62" stroke="#542B08" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <line x1="15" y1="79" x2="70" y2="79" stroke="#542B08" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
        <!-- Red Lac Wax Seal -->
        <circle cx="55" cy="115" r="16" fill="#881337"/>
        <circle cx="55" cy="115" r="13" fill="#BE123C"/>
        <circle cx="55" cy="115" r="7" fill="#881337"/>
        <path d="M 50,115 Q 55,108 60,115" stroke="#FFE4E6" stroke-width="1.2" fill="none"/>
      </g>

      <!-- Forearm & Embroidered Sleeve reaching from bottom-right -->
      <path d="M 180,320 L 70,120 L 15,145 L 120,340 Z" fill="url(#grad-lover-sleeve)"/>
      <path d="M 70,120 L 15,145" stroke="url(#grad-gold)" stroke-width="6"/>

      <!-- Masculine Palm & Knuckles Gripping Letter Gently -->
      <path d="M 25,120 C 10,95 -10,80 -35,75 C -55,70 -75,80 -85,100 C -75,125 -50,145 -15,150 Z" fill="#C68E6F"/>
      
      <!-- Knuckle Arc -->
      <circle cx="-25" cy="85" r="6" fill="#A8684D" opacity="0.4"/>
      <circle cx="-48" cy="88" r="6.5" fill="#A8684D" opacity="0.4"/>
      <circle cx="-68" cy="98" r="6" fill="#A8684D" opacity="0.4"/>

      <!-- Fingers wrapping around the letter edge -->
      <!-- Index Finger -->
      <path d="M -25,85 C -20,60 -15,35 -5,15 C 2,12 8,16 5,24 C -3,45 -10,70 -15,92 Z" fill="#D4997A"/>
      <ellipse cx="-4" cy="18" rx="4" ry="2.5" fill="#E8D5CE" transform="rotate(35 -4 18)"/>
      <!-- Middle Finger -->
      <path d="M -48,88 C -45,60 -40,32 -32,10 C -25,7 -20,11 -22,19 C -28,42 -35,68 -38,95 Z" fill="#C68E6F"/>
      <ellipse cx="-31" cy="12" rx="4" ry="2.5" fill="#E8D5CE" transform="rotate(25 -31 12)"/>
      <!-- Ring Finger (Wearing Emerald Signet Ring) -->
      <path d="M -68,98 C -65,72 -60,48 -52,28 C -46,25 -42,28 -44,35 C -50,55 -55,78 -58,105 Z" fill="#B8775B"/>
      <!-- Emerald Ring -->
      <rect x="-62" y="55" width="14" height="6" rx="1.5" fill="url(#grad-gold)" transform="rotate(18 -62 55)"/>
      <circle cx="-55" cy="58" r="3.5" fill="url(#grad-emerald)"/>
      <!-- Little Finger -->
      <path d="M -80,112 C -78,92 -74,72 -68,55 C -63,52 -60,55 -62,62 C -66,78 -70,96 -72,120 Z" fill="#A8684D"/>

      <!-- Thumb (Opposed from carpal heel, resting against front face of letter) -->
      <path d="M 15,130 C 5,120 -15,115 -35,122 C -45,125 -48,132 -42,136 C -25,142 -5,145 10,148 Z" fill="#D4997A"/>
      <ellipse cx="-40" cy="128" rx="4" ry="2.8" fill="#E8D5CE" transform="rotate(-15 -40 128)"/>
    </g>

    <!-- LEFT HAND (Resting over Heart, Fingers Cascading) -->
    <g transform="translate(240, 560)">
      <path d="M -160,280 L -60,110 L -10,135 L -100,300 Z" fill="url(#grad-lover-sleeve)"/>
      <path d="M -60,110 L -10,135" stroke="url(#grad-gold)" stroke-width="6"/>
      <!-- Palm over Heart -->
      <path d="M -15,115 C 5,90 25,75 50,70 C 70,68 85,78 95,95 C 85,120 60,138 25,142 Z" fill="#C68E6F"/>
      <!-- Relaxed cascading fingers -->
      <path d="M 45,72 C 60,55 78,42 98,36 C 104,38 105,44 100,48 C 82,56 68,68 55,85 Z" fill="#D4997A"/>
      <path d="M 68,78 C 85,62 105,52 125,48 C 130,50 131,56 126,60 C 108,68 92,80 78,98 Z" fill="#C68E6F"/>
      <path d="M 85,92 C 102,78 120,70 138,68 C 143,70 144,76 139,80 C 122,86 108,96 95,112 Z" fill="#B8775B"/>
    </g>

    <!-- Floating Illuminated Fireflies / Golden Motes -->
    <g id="s2-motes">
      <circle cx="310" cy="420" r="3" fill="#FFE885" opacity="0.8"/>
      <circle cx="430" cy="450" r="2.5" fill="#FFA826" opacity="0.7"/>
      <circle cx="270" cy="510" r="2" fill="#FFE885" opacity="0.6"/>
      <circle cx="460" cy="580" r="3.2" fill="#FFA826" opacity="0.85"/>
      <circle cx="350" cy="360" r="2.2" fill="#FFE885" opacity="0.75"/>
    </g>
  </g>

  <!-- ================= SCENE 3: THE COLD MIDNIGHT RAIN (8.8s - 13.5s) ================= -->
  <!-- "मेरा यह हाल होना सी" -->
  <g id="scene-3" opacity="0">
    <!-- Deep Stormy Indigo Atmosphere -->
    <rect width="720" height="1280" fill="url(#grad-night)"/>
    
    <!-- Heavy Storm Clouds & Lightning Flash Backing -->
    <path d="M 0,200 Q 180,120 360,180 T 720,150 L 720,400 L 0,400 Z" fill="#060F1A" opacity="0.85"/>
    
    <!-- Cold Rain-Streaked Mughal Arch Window -->
    <path d="M 0,0 L 720,0 L 720,1280 L 0,1280 Z 
             M 80,1180 L 80,380 
             C 80,310 106,275 150,255 
             C 178,218 224,190 280,180 
             C 318,142 360,105 360,95 
             C 360,105 402,142 440,180 
             C 496,190 542,218 570,255 
             C 614,275 640,310 640,380 
             L 640,1180 Z" fill="#060C14" fill-rule="evenodd"/>
    <!-- Wet Dark Stone Molding -->
    <path d="M 78,1180 L 78,380 C 78,310 104,275 148,255 C 176,218 222,190 278,180 C 316,142 360,105 360,95 C 360,105 404,142 442,180 C 498,190 544,218 572,255 C 616,275 642,310 642,380 L 642,1180" stroke="#1D3852" stroke-width="4" fill="none"/>

    <!-- Wet Marble Window Sill with Puddle Reflections -->
    <g transform="translate(80, 780)">
      <rect x="0" y="0" width="560" height="35" fill="#132638"/>
      <!-- Wet Reflection Sheen -->
      <rect x="20" y="4" width="520" height="8" rx="3" fill="#6BA4CC" opacity="0.35"/>
      <rect x="0" y="35" width="560" height="150" fill="#0A1520"/>
      <!-- Scattered Wilted Rose Petals in Rain -->
      <g fill="#881337">
        <path d="M 120,18 C 130,10 145,15 140,25 C 132,28 122,25 120,18 Z"/>
        <path d="M 280,22 C 290,14 305,18 298,28 C 290,30 282,28 280,22 Z"/>
        <path d="M 440,16 C 452,8 465,14 460,24 C 450,26 442,24 440,16 Z"/>
      </g>
    </g>

    <!-- SOLITARY HAND ON RAIN-DRENCHED SILL (Anidoodle Craft) -->
    <!-- Lover's wet hand resting motionless as rain drips from fingers -->
    <g id="s3-hand-wet" transform="translate(360, 740)">
      <!-- Dark Wet Brocade Sleeve -->
      <path d="M -160,250 L -60,60 L -10,75 L -90,270 Z" fill="#0A1624"/>
      <path d="M -60,60 L -10,75" stroke="#1D3852" stroke-width="5"/>
      <!-- Hand on Sill -->
      <path d="M -15,65 C 10,50 35,45 60,45 C 80,48 95,58 105,72 C 95,85 70,95 30,95 Z" fill="#8A6E62"/>
      <!-- Drooping Fingers resting on wet marble -->
      <path d="M 55,48 C 75,46 95,52 112,62 C 108,68 95,70 78,66 C 65,64 55,58 55,48 Z" fill="#9C7F72"/>
      <path d="M 75,52 C 98,52 120,60 138,72 C 132,78 118,80 100,75 C 85,72 75,64 75,52 Z" fill="#8A6E62"/>
      <path d="M 90,62 C 112,64 132,74 148,88 C 142,94 130,94 112,88 C 98,82 90,74 90,62 Z" fill="#785E53"/>
      <!-- Falling Raindrop from Fingertip -->
      <circle id="s3-drop" cx="148" cy="98" r="3" fill="#A8D4F5" opacity="0.85"/>
      <path d="M 148,95 L 148,115" stroke="#A8D4F5" stroke-width="1.8" stroke-linecap="round" opacity="0.6"/>
    </g>

    <!-- Extinguished Cold Brass Lantern (Smoke rising, glass wet) -->
    <g transform="translate(180, 480)">
      <line x1="0" y1="-120" x2="0" y2="0" stroke="#1D3852" stroke-width="2"/>
      <path d="M -24,0 C -24,-12 24,-12 24,0 Z" fill="#15283A"/>
      <rect x="-20" y="0" width="40" height="55" rx="4" fill="rgba(25, 45, 65, 0.4)" stroke="#1D3852" stroke-width="2"/>
      <!-- Dying Red Ember -->
      <circle cx="0" cy="35" r="4" fill="#FF3300"/>
      <circle cx="0" cy="35" r="8" fill="rgba(255, 60, 0, 0.3)"/>
      <!-- Organic Rising Curling Smoke into the rain -->
      <path id="s3-smoke" d="M 0,30 Q 15,-10 -8,-45 T 12,-90 T -10,-140" stroke="rgba(200, 220, 240, 0.55)" stroke-width="4" fill="none" stroke-linecap="round"/>
      <path d="M -24,55 L 24,55 L 14,68 L -14,68 Z" fill="#15283A"/>
    </g>
  </g>

  <!-- ================= SCENE 4: HOURGLASS OF FATE & CRESCENT MOON (13.5s - 18.17s) ================= -->
  <!-- "तेरा मिलना बहाना सी..." -->
  <g id="scene-4" opacity="0">
    <rect width="720" height="1280" fill="#04070D"/>
    <!-- Parting Clouds revealing Luminous Crescent Moon -->
    <circle cx="360" cy="320" r="260" fill="url(#grad-moon-glow)" opacity="0.75"/>
    
    <!-- Royal Crescent Moon (Chandramukhi) -->
    <g transform="translate(360, 320)">
      <path d="M -30,-60 
               A 70,70 0 1,0 60,30 
               A 60,60 0 1,1 -30,-60 Z" fill="#E8F4FD"/>
      <!-- Moon Craters & Surface Texture -->
      <circle cx="15" cy="-20" r="8" fill="#D0E3F2" opacity="0.6"/>
      <circle cx="32" cy="0" r="12" fill="#D0E3F2" opacity="0.6"/>
      <circle cx="-5" cy="25" r="9" fill="#D0E3F2" opacity="0.6"/>
    </g>

    <!-- Star Constellations in Clear Night Sky -->
    <g fill="#FFFFFF" opacity="0.8">
      <circle cx="140" cy="180" r="1.8"/><circle cx="210" cy="240" r="1.2"/>
      <circle cx="520" cy="190" r="1.8"/><circle cx="580" cy="270" r="1.5"/>
      <circle cx="180" cy="380" r="1.4"/><circle cx="540" cy="400" r="1.6"/>
    </g>

    <!-- Monumental Antique Brass Hourglass of Fate (Time & Destiny) -->
    <g id="s4-hourglass" transform="translate(360, 720)">
      <!-- Carved Teak Wood Stand -->
      <path d="M -90,130 L 90,130 L 70,110 L -70,110 Z" fill="url(#grad-gold)"/>
      <path d="M -90,-130 L 90,-130 L 70,-110 L -70,-110 Z" fill="url(#grad-gold)"/>
      <!-- Brass Pillars -->
      <line x1="-75" y1="-110" x2="-75" y2="110" stroke="url(#grad-gold)" stroke-width="6"/>
      <line x1="75" y1="-110" x2="75" y2="110" stroke="url(#grad-gold)" stroke-width="6"/>

      <!-- Hourglass Blown Glass Chambers -->
      <path d="M -60,-110 L 60,-110 
               C 50,-50 15,-15 10,0 
               C 15,15 50,50 60,110 
               L -60,110 
               C -50,50 -15,15 -10,0 
               C -15,-15 -50,-50 -60,-110 Z" fill="rgba(225, 240, 255, 0.12)" stroke="url(#grad-gold)" stroke-width="2.5"/>
      
      <!-- Upper Bulb Sand (Draining) -->
      <path id="s4-sand-top" d="M -45,-40 Q 0,-30 45,-40 L 10,0 L -10,0 Z" fill="#C41E3A"/>
      <!-- Trickling Stream of Crimson Sand / Petals -->
      <line x1="0" y1="0" x2="0" y2="90" stroke="#E11D48" stroke-width="2.5" stroke-dasharray="3,3"/>
      <!-- Lower Bulb Mound of Gathered Sand of Fate -->
      <path id="s4-sand-bottom" d="M -48,105 Q 0,70 48,105 Z" fill="#881337"/>
    </g>

    <!-- Drifting Lone Rose Petal Falling Gently across frame -->
    <path id="s4-drifting-petal" d="M 0,0 C 18,-10 32,5 25,20 C 15,25 0,18 0,0 Z" fill="#BE123C" transform="translate(360, 480)"/>

    <!-- Final Poetic Monument Calligraphy Seal -->
    <g id="s4-seal" transform="translate(360, 1020)">
      <line x1="-160" y1="-40" x2="160" y2="-40" stroke="url(#grad-gold)" stroke-width="1.5"/>
      <text y="-8" fill="#E8C96D" font-size="36" font-weight="700" text-anchor="middle" letter-spacing="4px">
        मोहब्बत सी, ज़माना सी
      </text>
      <text y="28" fill="#B39860" font-size="18" font-weight="400" text-anchor="middle" letter-spacing="5px">
        MOHABBAT SI ZAMANA SI // THE FATE
      </text>
      <line x1="-160" y1="50" x2="160" y2="50" stroke="url(#grad-gold)" stroke-width="1.5"/>
    </g>
  </g>

  <!-- ================= MASTER SUBTITLE LAYER (0.0s - 18.17s) ================= -->
  <g id="subtitle-layer">
    <!-- Subtitle Card 1 (0.2s - 4.4s): "मोहब्बत सी, ज़माना सी" -->
    <g id="sub-card-1" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(12, 4, 10, 0.92)" stroke="url(#grad-gold)" stroke-width="2"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        मोहब्बत सी, ज़माना सी
      </text>
      <text x="250" y="90" fill="#FFA726" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        MOHABBAT SI, ZAMANA SI
      </text>
      <text x="250" y="118" fill="#B88A28" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // AN ERA OF DEVOTION
      </text>
    </g>

    <!-- Subtitle Card 2 (4.5s - 8.7s): "यह दिल तेरा दीवाना सी" -->
    <g id="sub-card-2" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(12, 4, 10, 0.92)" stroke="url(#grad-gold)" stroke-width="2"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        यह दिल तेरा दीवाना सी
      </text>
      <text x="250" y="90" fill="#FF5252" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        YEH DIL TERA DEEWANA SI
      </text>
      <text x="250" y="118" fill="#B88A28" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // THIS HEART WAS YOURS ALONE
      </text>
    </g>

    <!-- Subtitle Card 3 (8.8s - 13.4s): "मेरा यह हाल होना सी" -->
    <g id="sub-card-3" transform="translate(110, 980)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(6, 12, 20, 0.94)" stroke="#6BA4CC" stroke-width="2"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        मेरा यह हाल होना सी...
      </text>
      <text x="250" y="90" fill="#90CAF9" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        MERA YEH HAAL HONA SI
      </text>
      <text x="250" y="118" fill="#64B5F6" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // THIS RUIN WAS DESTINED
      </text>
    </g>

    <!-- Subtitle Card 4 (13.5s - 18.17s): "तेरा मिलना बहाना सी" -->
    <g id="sub-card-4" transform="translate(110, 840)" opacity="0">
      <rect x="0" y="0" width="500" height="140" rx="12" fill="rgba(8, 4, 10, 0.94)" stroke="url(#grad-gold)" stroke-width="2"/>
      <text x="250" y="52" fill="#FFFFFF" font-size="32" font-weight="700" text-anchor="middle">
        तेरा मिलना बहाना सी...
      </text>
      <text x="250" y="90" fill="#FFE082" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="600" text-anchor="middle" letter-spacing="3px">
        TERA MILNA BAHANA SI
      </text>
      <text x="250" y="118" fill="#B88A28" font-size="13" font-weight="400" text-anchor="middle" letter-spacing="2px">
        // MEETING YOU WAS BUT FATE\'S PRETEXT
      </text>
    </g>
  </g>
</svg>

<canvas id="paper-canvas" width="720" height="1280"></canvas>
<canvas id="fx-canvas" width="720" height="1280"></canvas>

<script>
const DUR = 18.17;\nwindow.DUR = DUR;
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
    const val = Math.floor(215 + n * 40);
    data[i] = val;
    data[i+1] = Math.floor(val * 0.96);
    data[i+2] = Math.floor(val * 0.88);
    data[i+3] = 255;
  }
  pCtx.putImageData(imgData, 0, 0);
}

// 2. Dynamic Atmosphere FX (Motes, Rain, Drifting Petals)
function drawFX(t) {
  ctx.clearRect(0, 0, 720, 1280);

  if (t < 8.8) {
    // Act 1 & 2: Golden sunset dust motes & gentle floating petals
    const numMotes = 30;
    for (let i = 0; i < numMotes; i++) {
      const seed = i + 1;
      const baseX = 100 + pseudoRand(seed * 13) * 520;
      const baseY = 200 + pseudoRand(seed * 19) * 800;
      const spdY = 15 + pseudoRand(seed * 29) * 22;
      const curY = (baseY - t * spdY) % 800 + 200;
      const curX = baseX + Math.sin(t * 1.8 + seed) * 18;
      const sz = 1.2 + pseudoRand(seed * 37) * 2.2;
      const a = 0.3 + 0.5 * Math.sin(t * 3 + seed * 2);

      ctx.beginPath();
      ctx.arc(curX, curY, sz, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 215, 120, ${Math.max(0, a).toFixed(2)})`;
      ctx.fill();
    }
  } else if (t < 13.5) {
    // Act 3: Diagonal Cold Rain Streaks
    const numRain = 85;
    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'rgba(165, 210, 245, 0.45)';
    for (let i = 0; i < numRain; i++) {
      const seed = i + 1;
      const rx = (seed * 137.5 + t * 450) % 760 - 20;
      const ry = (seed * 219.3 + t * 950) % 1320 - 20;
      const len = 35 + pseudoRand(seed * 43) * 30;

      ctx.beginPath();
      ctx.moveTo(rx, ry);
      ctx.lineTo(rx - len * 0.35, ry + len);
      ctx.stroke();
    }
  } else {
    // Act 4: Drifting Rose Petals & Sparkling Stars
    const numPetals = 16;
    for (let i = 0; i < numPetals; i++) {
      const seed = i + 1;
      const px = 100 + pseudoRand(seed * 23) * 520 + Math.sin(t * 1.5 + seed) * 35;
      const py = (200 + (t - 13.5) * (35 + pseudoRand(seed * 11) * 35) + seed * 60) % 1000 + 100;
      const rot = t * 2 + seed;

      ctx.save();
      ctx.translate(px, py);
      ctx.rotate(rot);
      ctx.beginPath();
      ctx.ellipse(0, 0, 7, 4.5, 0, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(190, 24, 60, 0.65)';
      ctx.fill();
      ctx.restore();
    }
  }
}

// 3. Main Render Function
function render(t) {
  t = Math.max(0, Math.min(t, DUR));

  const s1 = document.getElementById('scene-1');
  const s2 = document.getElementById('scene-2');
  const s3 = document.getElementById('scene-3');
  const s4 = document.getElementById('scene-4');

  const sub1 = document.getElementById('sub-card-1');
  const sub2 = document.getElementById('sub-card-2');
  const sub3 = document.getElementById('sub-card-3');
  const sub4 = document.getElementById('sub-card-4');

  // Scene Visibility & Dissolves
  if (t < 4.5) {
    // Scene 1: Sunset Jharokha (0.0s - 4.5s)
    s1.style.display = 'inline';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Lantern subtle sway & pulse
    const lGlow = document.getElementById('s1-lantern-glow');
    const lFlame = document.getElementById('s1-lantern-flame');
    const sway = Math.sin(t * 2.2) * 4;
    const flick = 1 + 0.08 * Math.sin(t * 22) + 0.04 * Math.cos(t * 37);
    document.getElementById('s1-lantern').setAttribute('transform', `translate(360, 260) rotate(${sway.toFixed(1)} 0 -180)`);
    lFlame.setAttribute('transform', `scale(${flick.toFixed(3)})`);
    lGlow.setAttribute('r', (140 * flick).toFixed(1));

    // Dupatta wave
    const dup = document.getElementById('s1-dupatta');
    const dWave = Math.sin(t * 3.5) * 8;
    dup.setAttribute('d', `M 0,-15 C 30,${-25 + dWave} 70,${-10 - dWave} 110,${-18 + dWave} C 145,-25 180,-10 210,-20 C 185,15 150,5 110,12 C 70,20 30,10 0,25 Z`);

    // Dissolve out into Scene 2
    if (t > 4.1) {
      const outP = (t - 4.1) / 0.4;
      s1.setAttribute('opacity', (1 - outP).toFixed(2));
    } else {
      s1.setAttribute('opacity', '1');
    }
  } else if (t < 8.8) {
    // Scene 2: The Devoted Heart (4.5s - 8.8s)
    s1.style.display = 'none';
    s2.style.display = 'inline';
    s3.style.display = 'none';
    s4.style.display = 'none';

    // Heartbeat pulse on the letter & hands
    const beat = 1 + 0.04 * Math.sin(t * 6.2);
    document.getElementById('s2-hand-letter').setAttribute('transform', `translate(360, 520) scale(${beat.toFixed(3)})`);

    // Dissolve in & out
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
    // Scene 3: Cold Midnight Rain (8.8s - 13.5s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'inline';
    s4.style.display = 'none';

    // Raindrop drip animation
    const drop = document.getElementById('s3-drop');
    const dropProg = ((t - 8.8) * 2.8) % 1;
    drop.setAttribute('cy', (98 + dropProg * 45).toFixed(1));
    drop.setAttribute('opacity', (1 - dropProg).toFixed(2));

    // Smoke wisp curling
    const sm = document.getElementById('s3-smoke');
    const curl = Math.sin(t * 3.5) * 12;
    sm.setAttribute('d', `M 0,30 Q ${15 + curl},-10 ${-8 - curl},-45 T ${12 + curl},-90 T ${-10 - curl},-140`);

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
    // Scene 4: Hourglass of Fate & Moon (13.5s - 18.17s)
    s1.style.display = 'none';
    s2.style.display = 'none';
    s3.style.display = 'none';
    s4.style.display = 'inline';

    // Sand level in hourglass draining
    const sandP = (t - 13.5) / (18.17 - 13.5);
    const topY = -40 + sandP * 30;
    const botY = 105 - sandP * 35;
    document.getElementById('s4-sand-top').setAttribute('d', `M -45,${topY.toFixed(1)} Q 0,${(topY + 10).toFixed(1)} 45,${topY.toFixed(1)} L 10,0 L -10,0 Z`);
    document.getElementById('s4-sand-bottom').setAttribute('d', `M -48,105 Q 0,${botY.toFixed(1)} 48,105 Z`);

    // Drifting petal across moon
    const petY = 380 + sandP * 350;
    const petX = 360 + Math.sin(t * 2) * 90;
    const petRot = t * 45;
    document.getElementById('s4-drifting-petal').setAttribute('transform', `translate(${petX.toFixed(1)}, ${petY.toFixed(1)}) rotate(${petRot.toFixed(1)})`);

    if (t < 13.9) {
      const inP = (t - 13.5) / 0.4;
      s4.setAttribute('opacity', inP.toFixed(2));
    } else {
      s4.setAttribute('opacity', '1');
    }
  }

  // Subtitle Cards Stagger & Animations
  // Sub 1: 0.2s - 4.4s
  if (t >= 0.2 && t < 4.4) {
    const pIn = Math.min(1, (t - 0.2) / 0.35);
    const pOut = t > 4.0 ? Math.max(0, (4.4 - t) / 0.4) : 1;
    sub1.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub1.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub1.setAttribute('opacity', '0');
  }

  // Sub 2: 4.5s - 8.7s
  if (t >= 4.5 && t < 8.7) {
    const pIn = Math.min(1, (t - 4.5) / 0.35);
    const pOut = t > 8.3 ? Math.max(0, (8.7 - t) / 0.4) : 1;
    sub2.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub2.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub2.setAttribute('opacity', '0');
  }

  // Sub 3: 8.8s - 13.4s
  if (t >= 8.8 && t < 13.4) {
    const pIn = Math.min(1, (t - 8.8) / 0.35);
    const pOut = t > 13.0 ? Math.max(0, (13.4 - t) / 0.4) : 1;
    sub3.setAttribute('opacity', (pIn * pOut).toFixed(2));
    sub3.setAttribute('transform', `translate(110, ${(990 - pIn * 10).toFixed(1)})`);
  } else {
    sub3.setAttribute('opacity', '0');
  }

  // Sub 4: 13.5s - 18.17s
  if (t >= 13.5 && t <= 18.17) {
    const pIn = Math.min(1, (t - 13.5) / 0.35);
    sub4.setAttribute('opacity', pIn.toFixed(2));
    sub4.setAttribute('transform', `translate(110, ${(850 - pIn * 10).toFixed(1)})`);
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
      x0: 110, y0: 840, x1: 610, y1: 980
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
    f.write(html_content)

print('Generated index.html successfully! Length:', len(html_content))
