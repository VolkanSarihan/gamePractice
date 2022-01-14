def TerminatorMachineGun(p, enemy):
    enemy["hp"] = enemy["hp"]-p["power"] * 2

def TerminatorGrenade(p, enemy):
    enemy["hp"]= enemy["hp"]-p["power"] * 1.2
    
def VolcanoLavaLash(p, enemy):
    enemy["hp"]= enemy["hp"]-p["power"] * 1.3

def VolcanoTransform(p): # Volcano Hp -> 350 - Volcano Power -> 30
    p['hp'] = 350
    p['power'] = 30
    
def CannonDestroy(p, enemy):
    p['hp'] = p['hp'] * 0.9
    enemy['hp'] = enemy['hp'] * 0.8
    
def CannonHeal(p,):
    if p['hp']>60:
        p['hp'] = 75
    else:
        p['hp'] = p['hp'] + 15 
    

def attack(p,enemy):
    enemy["hp"]= enemy["hp"]-p["power"]

characters = [
    {
        'name': 'Terminator',
        'hp':250,
        'power':20,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':0,'cooldownLeft':0},
            {'name': 'Grenade', 'trigger': TerminatorGrenade,'type':'attack','cooldown':2,'cooldownLeft':3},
            {'name': 'Machine Gun', 'trigger': TerminatorMachineGun,'type':'attack','cooldown':3,'cooldownLeft':4}
        ]
    },
    {
        'name': 'Volcano',
        'hp':500,
        'power':5,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':0,'cooldownLeft':0},
            {'name': 'Lava Lash:', 'trigger': VolcanoLavaLash,'type':'attack','cooldown':3,'cooldownLeft':4},
            {'name': 'Transform', 'trigger': VolcanoTransform,'type':'utility','cooldown':100,'cooldownLeft':101}
        ]
    },
    {
        'name': 'GlassCannon',
        'hp':75,
        'power':50,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack,'type':'attack','cooldown':0,'cooldownLeft':0},
            {'name': 'Destroy', 'trigger': CannonDestroy,'type':'attack','cooldown':3,'cooldownLeft':4},
            {'name': 'Heal', 'trigger': CannonHeal,'type':'utility','cooldown':4,'cooldownLeft':5}
        ]
    }
]

print('Characters:')

for i,character in enumerate(characters):
    for key,value in character.items():
        if key == 'skills':
            pass 
        else:
            print(str(i)+" "+key,value, sep=' - ', end=' ')
    print()

p1=characters[int(input("p1 choose your character: "))]
p2=characters[int(input("p2 choose your character: "))]

print(f"p1 ={p1['name']}, p2={p2['name']}")

while p1["hp"]>0 and p2["hp"]>0:
    print(p1['name'], p1['hp'])
    for key, value in p1.items():
        if key == 'skills':
            for i,skill in enumerate(value):
                print(i, skill['name'])
    
    p1Skill = p1['skills'][int(input('Select skill: '))]
    
        
    if p1Skill['type'] =='attack':
        p1Skill['trigger'](p1, p2)
    else:
        p1Skill['trigger'](p1)
    print(p1['name'], p1['hp'])
    print(p2['name'], p2['hp'])
    
    if 0>=p2 ['hp']:
        break
    print(p2['name'], p2['hp'])
    for key, value in p2.items():
        if key == 'skills':
            for i,skill in enumerate(value):
                print(i, skill['name'])
    
    p2Skill = p2['skills'][int(input('Select skill: '))]
    if p2Skill['type'] =='attack':
        p2Skill['trigger'](p2, p1)
    else:
        p2Skill['trigger'](p2)
    print(p2['name'], p2['hp'])
    print(p1['name'], p1['hp'])
    
    
    # TODO Select Skill DONE
    # TODO Solve Heal Attack function problem Done
    # TODO ADD cooldown to skills
    # TODO Add mana cost to skills


if p1["hp"]>0:
    print(f"WINNER!! :P1 {p1['name']}")
else:
    print(f"WINNER!! :P2 {p2['name']}")
