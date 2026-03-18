import json

with open('vocabulary.json', 'r') as f:
    data = json.load(f)

tom_updates = {
    'perspective': {
        'special': 'Home Free (2024)',
        'context': "Sometimes you just need <b>perspective</b>, to know that you're doing all right. You know? I go to shitty bars. You ever do that? Every town's got one. Go in there in the middle of the afternoon and buy drinks for the 80-year-old guy sitting at that little crummy bar, under the saddest Christmas lights of all time. Listen to his stories. How he fought in every war, lost money in every recession, has every STD known to man. After an hour of that, you come back out into the light. You're like, 'I think I can do this. I'm gonna be all right.'"
    },
    'compartmentalize': {
        'special': 'Home Free (2024)',
        'context': "My wife does it. She gets impatient. She grabs it and looks at me. 'You sissy.' And takes it outside. I'll be honest with you. That's why I don't like hers sometimes. Now I've got to <b>compartmentalize</b> that I'm not married to old 'Rat Fingers' Johnson."
    },
    'epitome': {
        'special': 'What A Day (2022)',
        'context': "The <b>epitome</b> of male vanity is in the summer. In the summer, in any town, you will see a man, an 80-year-old man, walking down the street in a tank top, or worse, no shirt at all. Just strutting down the sidewalk like an expired rotisserie chicken. No muscle mass left, just two bony chicken wings. Licorice nipples swaying in the wind. Gold chains tangled in his spooky cobweb body hair."
    },
    'flippantly': {
        'special': 'Home Free (2024)',
        'context': "Raising kids is no joke. It's no joke. If you don't have children, people approach you all the time very <b>flippantly</b>. 'When are you gonna do it? You should have kids.' 'When are you gonna have kids?' No. You should think long and hard about whether you're gonna have kids."
    },
    'immaculate': {
        'special': "You're Doing Great (2020)",
        'context': "I was walking down Sixth Avenue in New York, this businessman walking the other way. So well thought out, everything <b>immaculate</b>: suit, tie, leather shoes match his briefcase, glasses, not a hair out of place. Fly open, one ball out. I understood. He did everything on the list, didn't check that one box."
    }
}

fixed = 0
for e in data:
    if e.get('comedian') == 'Tom Papa':
        word = e.get('word', '')
        if word in tom_updates:
            e['special'] = tom_updates[word]['special']
            e['context'] = tom_updates[word]['context']
            # Set appropriate image
            if 'Home Free' in e['special']:
                e['image'] = 'images/tom-papa-home-free-2024-transcript.webp'
            elif 'What A Day' in e['special']:
                e['image'] = 'images/tom-papa-what-a-day-2022-transcript.webp'
            elif "You're Doing Great" in e['special']:
                e['image'] = 'images/tom-papa-youre-doing-great-2020-transcript.webp'
            fixed += 1

print(f"Fixed {fixed} Tom Papa entries")

with open('vocabulary.json', 'w') as f:
    json.dump(data, f, indent=2)

# Verify no more placeholders
placeholders = []
for e in data:
    context = e.get('context', '')
    if any(pattern in context.lower() for pattern in ['papa uses', 'describing', 'used when', 'term used']):
        placeholders.append((e.get('comedian'), e.get('word')))

print(f"\nRemaining placeholder descriptions: {len(placeholders)}")
if placeholders:
    for comedian, word in placeholders:
        print(f"  {comedian}: {word}")
PYEOF