import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TL = json.load(open(os.path.join(HERE, 'timeline.json'), encoding='utf-8'))
cues = [
    {
        't0': round(v['t0'], 3),
        't1': round(v['t0'] + v['dur'] + 0.35, 3),
        'text': v['text'],
    }
    for v in TL['voices']
]
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
json.dump(cues, open(os.path.join(HERE, 'out', 'cues.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('Wrote out/cues.json:', len(cues), 'cues')

