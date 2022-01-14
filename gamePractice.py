def TerminatorMachineGun(p, enemy):
    enemy["hp"] = enemy["hp"]-p["power"] * 2

def TerminatorGrenade(p, enemy):
    enemy["hp"] = enemy["hp"]-p["power"] * 1.2
    
def VolcanoLavaLash(p, enemy):
    enemy["hp"] = enemy["hp"]-p["power"] * 1.3

def VolcanoTransform(p): # Volcano Hp -> 350 - Volcano Power -> 30
    p['hp'] = 350
    p['power'] = 30
    
def CannonDestroy(p, enemy):
    p['hp'] = p['hp'] * 0.9
    enemy['hp'] = enemy['hp'] * 0.8
    
def CannonHeal(p,):
    if p['hp'] > 60:
        p['hp'] = 75
    else:
        p['hp'] = p['hp'] + 15 
    

def attack(p, enemy):
    enemy["hp"] = enemy["hp"] - p["power"]

characters = [
    {
        'name': 'Terminator',
        'hp':250,
        'power':20,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':1,'cooldownLeft':0},
            {'name': 'Grenade', 'trigger': TerminatorGrenade,'type':'attack','cooldown':3,'cooldownLeft':0},
            {'name': 'Machine Gun', 'trigger': TerminatorMachineGun,'type':'attack','cooldown':4,'cooldownLeft':0}
        ]
    },
    {
        'name': 'Volcano',
        'hp':500,
        'power':5,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':1,'cooldownLeft':0},
            {'name': 'Lava Lash:', 'trigger': VolcanoLavaLash,'type':'attack','cooldown':4,'cooldownLeft':0},
            {'name': 'Transform', 'trigger': VolcanoTransform,'type':'utility','cooldown':101,'cooldownLeft':0}
        ]
    },
    {
        'name': 'GlassCannon',
        'hp':75,
        'power':50,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':1,'cooldownLeft':0},
            {'name': 'Destroy', 'trigger': CannonDestroy,'type':'attack','cooldown':4,'cooldownLeft':0},
            {'name': 'Heal', 'trigger': CannonHeal,'type':'utility','cooldown':5,'cooldownLeft':0}
        ]
    }
]

print('Characters:')

for i, character in enumerate(characters):
    for key, value in character.items():
        if key == 'skills':
            pass 
        else:
            print(str(i) + " " + key, value, sep = ' - ', end=' ')
    print()

p1 = characters[int(input("p1 choose your character: "))]
p2 = characters[int(input("p2 choose your character: "))]

print(f"p1 ={p1['name']}, p2={p2['name']}")

while p1["hp"] > 0 and p2["hp"] > 0:
    for key, value in p1.items():
        if key == 'skills':
            for i, skill in enumerate(value):
                print(i, skill['name'], skill['cooldownLeft'])
                
    p1Skill = p1['skills'][int(input('Select skill: '))]            
    while True: # ???????????????????
        if p1Skill['cooldownLeft'] == 0:
            if p1Skill['type'] =='attack':
                p1Skill['trigger'](p1, p2)
            else:
                p1Skill['trigger'](p1)
            break
        else:
            p1Skill = p1['skills'][int(input('Skill on cooldown. Select another skill: '))] 
        
    p1Skill['cooldownLeft'] = p1Skill['cooldown']
    
    for item in p1['skills']:
        if item['cooldownLeft'] != 0:
            item['cooldownLeft'] -= 1
    
    print(p1['name'], p1['hp'])
    if 0>=p2 ['hp']:
        break
    
    print(p2['name'], p2['hp'])
    for key, value in p2.items():
        if key == 'skills':
            for i,skill in enumerate(value):
                print(i, skill['name'], skill['cooldownLeft'])
                
    p2Skill = p2['skills'][int(input('Select skill: '))]
    while True:
        if p2Skill['cooldownLeft'] == 0: 
            if p2Skill['type'] =='attack':
                p2Skill['trigger'](p2, p1)
            else:
                p2Skill['trigger'](p2)
            break
        else:
            p2Skill = p2['skills'][int(input('Skill on cooldown. Select another skill: '))] 
    
    p2Skill['cooldownLeft'] = p2Skill['cooldown']
    
    for item in p2['skills']:
        if item['cooldownLeft'] != 0:
            item['cooldownLeft'] -= 1
            
    print(p2['name'], p2['hp'])
    
    
    # TODO Select Skill DONE
    # TODO Solve Heal Attack function problem DONE
    # TODO ADD cooldown to skills DONE
    # TODO Add mana cost to skills
    # TODO ADD one time skills (Volcano -> Transform skill)

if p1["hp"]>0:
    print(f"WINNER!! :P1 {p1['name']}")
else:
    print(f"WINNER!! :P2 {p2['name']}")