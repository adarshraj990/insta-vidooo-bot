import os

with open(r'c:\Users\Adarsh\Desktop\vidooo\meri-mehfil\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add defs before </defs>
extra_defs = '''
    <!-- Sleeve & Attire Gradients for Lovers in Prologue -->
    <linearGradient id="grad-jade-sleeve" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#082417"/>
      <stop offset="50%" stop-color="#11422C"/>
      <stop offset="100%" stop-color="#061A10"/>
    </linearGradient>

    <linearGradient id="grad-burgundy-sleeve" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#470613"/>
      <stop offset="50%" stop-color="#7A1024"/>
      <stop offset="100%" stop-color="#38030D"/>
    </linearGradient>

    <!-- Divine Union Aura (Warm Golden Sunburst between hands) -->
    <radialGradient id="grad-union-aura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF6D4" stop-opacity="1"/>
      <stop offset="30%" stop-color="#FFA726" stop-opacity="0.75"/>
      <stop offset="65%" stop-color="#E65100" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#180206" stop-opacity="0"/>
    </radialGradient>

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
'''

if 'id="grad-jade-sleeve"' not in text:
    text = text.replace('</defs>', extra_defs + '  </defs>')

# 2. Replace prologue block
p_start = text.find('<g id="scene-prologue">')
p_end = text.find('<!-- ================= SCENE: DIPTYCH')

new_prologue = '''<g id="scene-prologue">
    <rect width="720" height="1280" fill="#140206"/>
    <!-- Deep Royal Crimson Vignette Background -->
    <circle cx="360" cy="640" r="520" fill="#22040B"/>
    <circle cx="360" cy="640" r="380" fill="#360612"/>
    <circle cx="360" cy="640" r="240" fill="#4A091A"/>

    <!-- Central Warm Illuminating Aura behind meeting hands -->
    <g id="p-union-glow" transform="translate(360, 640)">
      <circle cx="0" cy="0" r="280" fill="url(#grad-union-aura)" opacity="0.95"/>
      <circle cx="0" cy="0" r="140" fill="#FFE8A3" opacity="0.18"/>
    </g>

    <!-- Floating subtle golden embers/motes in the warm light -->
    <g id="p-motes">
      <circle cx="340" cy="610" r="2.5" fill="#FFEAA7" opacity="0.7"/>
      <circle cx="380" cy="660" r="1.8" fill="#FFD166" opacity="0.6"/>
      <circle cx="320" cy="690" r="2.0" fill="#FFEAA7" opacity="0.5"/>
      <circle cx="410" cy="620" r="1.5" fill="#FFD166" opacity="0.7"/>
      <circle cx="360" cy="570" r="2.2" fill="#FFEAA7" opacity="0.8"/>
      <circle cx="290" cy="640" r="1.6" fill="#FFD166" opacity="0.5"/>
    </g>

    <!-- MAN'S HAND & ARM (Left lover reaching from bottom-left) -->
    <!-- Modeled with true anatomical proportions: knuckle arc, 14 phalanges, opposed thumb, emerald signet ring -->
    <g id="p-hand-man" transform="translate(0, 0)">
      <!-- Royal Mughal Angrakha Sleeve (Forest Jade & Gold) -->
      <path d="M -50,1300 L 120,880 L 220,935 L 70,1320 Z" fill="url(#grad-jade-sleeve)"/>
      <!-- Gold Zari Embroidery on Sleeve -->
      <path d="M 80,900 L 180,955" stroke="#C29D38" stroke-width="6"/>
      <path d="M 85,892 L 185,947" stroke="#FFF2B2" stroke-width="2"/>
      <path d="M 95,920 L 195,975" stroke="#C29D38" stroke-width="3" stroke-dasharray="4,6"/>
      <!-- Pearl cuff border -->
      <g transform="translate(105, 875) rotate(32)">
        <circle cx="0" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="12" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="24" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="36" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="48" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="60" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="72" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="84" cy="0" r="4.5" fill="url(#grad-pearl)"/>
        <circle cx="96" cy="0" r="4.5" fill="url(#grad-pearl)"/>
      </g>

      <!-- Forearm & Carpal Heel (Warm Olive Skin) -->
      <path d="M 120,880 C 145,830 180,780 220,740 L 290,785 C 260,835 220,890 190,935 Z" fill="#B87B5E"/>
      <path d="M 130,870 C 152,825 185,780 222,745 L 285,785 C 255,830 215,880 188,925 Z" fill="#C68E6F"/>
      <!-- Wrist Tendon & Shading -->
      <path d="M 195,810 Q 230,815 250,770" stroke="#9E654C" stroke-width="2.5" fill="none" opacity="0.6"/>

      <!-- Palm & Dorsal Metacarpals following Knuckle Arc -->
      <path d="M 220,740 C 235,710 260,685 295,665 C 325,650 350,655 365,675 C 350,715 325,755 290,785 Z" fill="#C68E6F"/>
      
      <!-- Knuckle Arc Shading (Index, Middle, Ring, Little) -->
      <circle cx="275" cy="700" r="7" fill="#B37355" opacity="0.5"/>
      <circle cx="305" cy="675" r="7.5" fill="#B37355" opacity="0.5"/>
      <circle cx="335" cy="665" r="7.5" fill="#B37355" opacity="0.5"/>
      <circle cx="360" cy="672" r="6.5" fill="#B37355" opacity="0.5"/>

      <!-- Man's Thumb (Opposed from wrist, resting forward) -->
      <path d="M 215,745 C 230,755 255,765 275,760 C 295,755 315,745 330,735 C 322,725 305,732 285,738 C 265,742 240,735 228,730 Z" fill="#C68E6F"/>
      <!-- Thumb nail -->
      <ellipse cx="325" cy="735" rx="5" ry="3.5" fill="#E8D5CE" transform="rotate(-15 325 735)"/>

      <!-- Man's Little Finger (Curled naturally in cascade) -->
      <path d="M 358,680 C 375,690 395,705 405,720 C 410,727 405,732 398,730 C 388,720 372,705 352,692 Z" fill="#A8684D"/>

      <!-- Man's Ring Finger (Supporting cascade) -->
      <path d="M 335,665 C 358,670 385,680 405,695 C 412,700 408,707 400,705 C 380,690 355,680 330,675 Z" fill="#B8775B"/>

      <!-- Man's Middle Finger (Longest, reaching to touch her hand) -->
      <path d="M 305,675 C 325,650 350,635 375,630 C 385,628 388,634 380,640 C 355,652 330,670 300,688 Z" fill="#C68E6F"/>
      <!-- Middle finger nail -->
      <ellipse cx="377" cy="632" rx="4.5" ry="3" fill="#E8D5CE" transform="rotate(-18 377 632)"/>

      <!-- Man's Index Finger (Curving forward tenderly, wearing Emerald Ring) -->
      <path d="M 275,700 C 295,680 320,660 348,642 C 358,636 362,642 355,648 C 328,670 300,695 270,715 Z" fill="#D4997A"/>
      <!-- Index finger nail -->
      <ellipse cx="354" cy="642" rx="4.5" ry="3" fill="#E8D5CE" transform="rotate(-28 354 642)"/>

      <!-- Royal Emerald Signet Ring on Index Finger -->
      <g transform="translate(315, 665) rotate(-35)">
        <rect x="-3" y="-8" width="6" height="16" rx="2" fill="url(#grad-gold)"/>
        <rect x="-5" y="-5" width="10" height="10" rx="2" fill="url(#grad-gold)"/>
        <circle cx="0" cy="0" r="4.2" fill="url(#grad-emerald)"/>
        <circle cx="-1" cy="-1" r="1.5" fill="#A7F3D0" opacity="0.8"/>
      </g>
    </g>

    <!-- WOMAN'S HAND & ARM (Right beloved reaching from bottom-right) -->
    <!-- Modeled with delicate feminine anatomy, henna mandala, red/gold bangles, ruby ring -->
    <g id="p-hand-woman" transform="translate(0, 0)">
      <!-- Royal Mughal Silk Sleeve (Crimson / Burgundy Velvet) -->
      <path d="M 770,1300 L 600,880 L 500,935 L 650,1320 Z" fill="url(#grad-burgundy-sleeve)"/>
      <!-- Gold Zari Cuff Embroidery -->
      <path d="M 620,900 L 520,955" stroke="#C29D38" stroke-width="6"/>
      <path d="M 615,892 L 515,947" stroke="#FFF2B2" stroke-width="2"/>
      <path d="M 605,920 L 505,975" stroke="#C29D38" stroke-width="3" stroke-dasharray="4,6"/>

      <!-- Stacked Royal Bangles (Choodiyan: Gold Kadas + Red Lac Glass Bangles) -->
      <g transform="translate(560, 860) rotate(-32)">
        <rect x="-55" y="0" width="10" height="70" rx="3" fill="url(#grad-gold)"/>
        <rect x="-42" y="3" width="4" height="64" rx="2" fill="#B31226"/>
        <rect x="-36" y="3" width="4" height="64" rx="2" fill="#B31226"/>
        <rect x="-30" y="3" width="4" height="64" rx="2" fill="#B31226"/>
        <rect x="-24" y="3" width="4" height="64" rx="2" fill="#B31226"/>
        <rect x="-17" y="1" width="9" height="68" rx="3" fill="url(#grad-gold)"/>
        <circle cx="-50" cy="10" r="2.5" fill="url(#grad-pearl)"/>
        <circle cx="-50" cy="25" r="2.5" fill="url(#grad-pearl)"/>
        <circle cx="-50" cy="40" r="2.5" fill="url(#grad-pearl)"/>
        <circle cx="-50" cy="55" r="2.5" fill="url(#grad-pearl)"/>
      </g>

      <!-- Slender Feminine Forearm & Carpal Heel -->
      <path d="M 600,880 C 575,830 540,780 500,740 L 430,785 C 460,835 500,890 530,935 Z" fill="#BA735A"/>
      <path d="M 590,870 C 568,825 535,780 498,745 L 435,785 C 465,830 505,880 532,925 Z" fill="#DE9C80"/>

      <!-- Palm & Dorsal Metacarpals following Feminine Knuckle Arc -->
      <path d="M 500,740 C 485,710 460,685 425,665 C 395,650 370,655 355,675 C 370,715 395,755 430,785 Z" fill="#DE9C80"/>

      <!-- INTRICATE HENNA / MEHNDI ART (Dorsal Mandala & Finger Jaal) -->
      <!-- Central Circular Floral Mandala -->
      <g transform="translate(435, 715)">
        <circle cx="0" cy="0" r="22" fill="none" stroke="#521508" stroke-width="2.5"/>
        <circle cx="0" cy="0" r="15" fill="#521508" opacity="0.85"/>
        <circle cx="0" cy="0" r="9" fill="#DE9C80"/>
        <circle cx="0" cy="0" r="4" fill="#521508"/>
        <path d="M 0,-24 L 3,-18 L -3,-18 Z M 0,24 L 3,18 L -3,18 Z M -24,0 L -18,3 L -18,-3 Z M 24,0 L 18,3 L 18,-3 Z M -17,-17 L -12,-16 L -16,-12 Z M 17,17 L 12,16 L 16,12 Z M -17,17 L -12,16 L -16,12 Z M 17,-17 L 12,-16 L 16,-12 Z" fill="#521508"/>
        <circle cx="0" cy="-28" r="1.5" fill="#521508"/>
        <circle cx="20" cy="-20" r="1.5" fill="#521508"/>
        <circle cx="28" cy="0" r="1.5" fill="#521508"/>
        <circle cx="20" cy="20" r="1.5" fill="#521508"/>
        <circle cx="0" cy="28" r="1.5" fill="#521508"/>
        <circle cx="-20" cy="20" r="1.5" fill="#521508"/>
        <circle cx="-28" cy="0" r="1.5" fill="#521508"/>
        <circle cx="-20" cy="-20" r="1.5" fill="#521508"/>
      </g>

      <!-- Woman's Thumb (Reaching tenderly towards his thumb) -->
      <path d="M 505,745 C 490,755 465,765 445,760 C 425,755 405,745 390,735 C 398,725 415,732 435,738 C 455,742 480,735 492,730 Z" fill="#DE9C80"/>
      <path d="M 390,735 C 395,730 405,732 410,740 C 400,744 394,740 390,735 Z" fill="#521508"/>
      <ellipse cx="395" cy="735" rx="4" ry="2.8" fill="#F3E5E0" transform="rotate(15 395 735)"/>

      <!-- Woman's Little Finger (Gracefully arched outward) -->
      <path d="M 362,680 C 345,690 325,705 315,720 C 310,727 315,732 322,730 C 332,720 348,705 368,692 Z" fill="#B36E53"/>
      <circle cx="317" cy="722" r="4" fill="#521508"/>

      <!-- Woman's Ring Finger (Touching softly, adorned with Ruby Ring) -->
      <path d="M 385,665 C 362,670 335,680 315,695 C 308,700 312,707 320,705 C 340,690 365,680 390,675 Z" fill="#CD8469"/>
      <circle cx="314" cy="699" r="4.2" fill="#521508"/>

      <!-- Haathphool Gold Chain from Wrist to Ring -->
      <path d="M 500,780 Q 430,730 355,680" stroke="#D4AF37" stroke-width="1.8" fill="none" stroke-dasharray="3,3"/>

      <!-- Ruby Ring on Ring Finger -->
      <g transform="translate(355, 680) rotate(35)">
        <rect x="-2.5" y="-7" width="5" height="14" rx="1.5" fill="url(#grad-gold)"/>
        <path d="M 0,-7 C 5,-2 5,4 0,7 C -5,4 -5,-2 0,-7 Z" fill="url(#grad-ruby)"/>
        <circle cx="0" cy="1" r="1.5" fill="#FECDD3" opacity="0.8"/>
      </g>

      <!-- Woman's Middle Finger (Longest, intertwining with his middle finger) -->
      <path d="M 415,675 C 395,650 370,635 345,630 C 335,628 332,634 340,640 C 365,652 390,670 420,688 Z" fill="#DE9C80"/>
      <path d="M 345,630 C 338,632 334,636 340,642 C 348,640 352,634 345,630 Z" fill="#521508"/>
      <ellipse cx="343" cy="632" rx="4" ry="2.8" fill="#F3E5E0" transform="rotate(18 343 632)"/>

      <!-- Woman's Index Finger (Touching his index/thumb) -->
      <path d="M 445,700 C 425,680 400,660 372,642 C 362,636 358,642 365,648 C 392,670 420,695 450,715 Z" fill="#E8A98E"/>
      <path d="M 372,642 C 365,644 362,648 368,652 C 375,650 378,645 372,642 Z" fill="#521508"/>
      <ellipse cx="366" cy="642" rx="4" ry="2.8" fill="#F3E5E0" transform="rotate(28 366 642)"/>
    </g>

    <!-- Cold Shadow / Night Vignette Overlay (activates on parting) -->
    <rect id="p-cold-shadow" width="720" height="1280" fill="#040914" opacity="0" pointer-events="none"/>

    <!-- Prologue Calligraphy Title Card -->
    <g id="p-title-card" transform="translate(360, 1050)">
      <text y="0" fill="#E8C96D" font-size="44" font-weight="700" text-anchor="middle" letter-spacing="4px">
        मेरी महफ़िल
      </text>
      <text y="48" fill="#B39860" font-size="22" font-weight="400" text-anchor="middle" letter-spacing="5px">
        MERI MEHFIL // A SILENT GHAZAL
      </text>
      <line x1="-140" y1="70" x2="140" y2="70" stroke="#D4AF37" stroke-width="1.5"/>
    </g>
  </g>

  '''

text = text[:p_start] + new_prologue + text[p_end:]

# 3. Update render(t) prologue logic
old_render_part = """    const pHand = document.getElementById('p-hand');
    const pFlameGroup = document.getElementById('p-flame-group');
    const pSmokeGroup = document.getElementById('p-smoke-group');
    const pSmokeCore = document.getElementById('p-smoke-core');
    const pSmokeBillow = document.getElementById('p-smoke-billow');

    if (t < 1.8) {
      // Hand descends towards flame with natural cubic ease
      const p = Math.min(1, t / 1.7);
      const ease = 1 - Math.pow(1 - p, 3);
      const hX = 560 - ease * 160;
      const hY = 340 + ease * 170;
      pHand.setAttribute('transform', `translate(${hX.toFixed(1)}, ${hY.toFixed(1)})`);

      // Flame flickers organically
      const flick = 1 + 0.08 * Math.sin(t * 26) + 0.04 * Math.cos(t * 43);
      pFlameGroup.setAttribute('transform', `scale(${flick.toFixed(3)})`);
      pFlameGroup.setAttribute('opacity', '1');
      pSmokeGroup.setAttribute('opacity', '0');
    } else {
      // Flame extinguished!
      const pAfter = t - 1.8;
      pFlameGroup.setAttribute('opacity', Math.max(0, 1 - pAfter * 8).toFixed(2));
      pSmokeGroup.setAttribute('opacity', Math.min(1, pAfter * 3).toFixed(2));

      // Organic rising curling smoke
      const sProg = pAfter * 75;
      const curl1 = Math.sin(t * 5) * 22;
      const curl2 = Math.cos(t * 4) * 28;
      pSmokeCore.setAttribute('d', `M 40,-20 Q ${25 + curl1},-80 ${60 - curl2},-${150 + sProg} T ${30 + curl1},-${250 + sProg * 1.4}`);
      pSmokeBillow.setAttribute('d', `M 40,-20 Q ${55 - curl1},-90 ${20 + curl2},-${160 + sProg} T ${50 - curl1},-${260 + sProg * 1.3}`);

      // Hand gently withdraws
      const wProg = Math.min(1, pAfter / 1.2);
      const wEase = wProg * wProg;
      pHand.setAttribute('transform', `translate(${(400 + wEase * 110).toFixed(1)}, ${(510 - wEase * 80).toFixed(1)})`);
    }

    if (t >= 2.8) {
      sPrologue.setAttribute('opacity', ((3.2 - t) / 0.4).toFixed(2));
    } else {
      sPrologue.setAttribute('opacity', '1');
    }"""

new_render_part = """    const pHandMan = document.getElementById('p-hand-man');
    const pHandWoman = document.getElementById('p-hand-woman');
    const pUnionGlow = document.getElementById('p-union-glow');
    const pColdShadow = document.getElementById('p-cold-shadow');
    const pMotes = document.getElementById('p-motes');

    if (t < 1.6) {
      // 0.0s - 1.6s: Tender union & breathing hold
      const breath = Math.sin(t * 2.5) * 3;
      pHandMan.setAttribute('transform', `translate(${(-breath * 0.5).toFixed(1)}, ${(breath).toFixed(1)})`);
      pHandWoman.setAttribute('transform', `translate(${(breath * 0.5).toFixed(1)}, ${(breath).toFixed(1)})`);

      const glowPulse = 0.9 + 0.1 * Math.sin(t * 4);
      pUnionGlow.setAttribute('opacity', glowPulse.toFixed(2));
      pColdShadow.setAttribute('opacity', '0');
      sPrologue.setAttribute('opacity', '1');
    } else if (t < 2.9) {
      // 1.6s - 2.9s: "Meri mehfil mein karke andhere..." - The Parting!
      const p = (t - 1.6) / 1.3;
      const easeW = p * p * (3 - 2 * p); // smoothstep
      
      // Woman's hand gently recedes into her world (to the right and down)
      const wX = easeW * 340;
      const wY = easeW * 220;
      const wRot = easeW * 12;
      pHandWoman.setAttribute('transform', `translate(${wX.toFixed(1)}, ${wY.toFixed(1)}) rotate(${wRot.toFixed(1)} 500 740)`);

      // Man's hand lingers, stretches slightly towards her, then sinks into cold loneliness
      let mX = 0, mY = 0;
      if (p < 0.35) {
        const reach = p / 0.35;
        mX = reach * 14;
        mY = -reach * 10;
      } else {
        const fall = (p - 0.35) / 0.65;
        const fallEase = fall * fall;
        mX = 14 - fallEase * 28;
        mY = -10 + fallEase * 48;
      }
      pHandMan.setAttribute('transform', `translate(${mX.toFixed(1)}, ${mY.toFixed(1)})`);

      // Light fades, darkness engulfs his side
      const glowFade = Math.max(0, 1 - p * 1.4);
      pUnionGlow.setAttribute('opacity', glowFade.toFixed(2));
      pMotes.setAttribute('opacity', glowFade.toFixed(2));
      
      // Cold shadow deepens
      const shadowRise = Math.min(0.85, p * 0.95);
      pColdShadow.setAttribute('opacity', shadowRise.toFixed(2));
      sPrologue.setAttribute('opacity', '1');
    } else {
      // 2.9s - 3.2s: Seamless crossfade into the Diptych
      const xfade = (t - 2.9) / 0.3;
      sPrologue.setAttribute('opacity', Math.max(0, 1 - xfade).toFixed(2));
      sDiptych.style.display = 'inline';
      sDiptych.setAttribute('opacity', Math.min(1, xfade).toFixed(2));
    }"""

assert old_render_part in text, "old_render_part not found!"
text = text.replace(old_render_part, new_render_part)

with open(r'c:\Users\Adarsh\Desktop\vidooo\meri-mehfil\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html successfully! New length:', len(text))
