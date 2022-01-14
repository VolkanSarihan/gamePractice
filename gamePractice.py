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
    
def CannonHeal(p):
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
            {'name': 'Basic Attack', 'trigger': attack},
            {'name': 'Grenade', 'trigger': TerminatorGrenade},
            {'name': 'Machine Gun', 'trigger': TerminatorMachineGun}
        ]
    },
    {
        'name': 'Volcano',
        'hp':500,
        'power':5,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack},
            {'name': 'Lava Lash', 'trigger': VolcanoLavaLash},
            {'name': 'Transform', 'trigger': VolcanoTransform}
        ]
    },
    {
        'name': 'GlassCannon',
        'hp':75,
        'power':50,
        'skills': [
            {'name': 'Basic Attack', 'trigger': attack},
            {'name': 'Destroy', 'trigger': CannonDestroy},
            {'name': 'Heal', 'trigger': CannonHeal}
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
    
    p1Skill = int(input('Select skill: ')) # 2
    
    p1['skills'][p1Skill]['trigger'](p1, p2)
    
    print(p1['name'], p1['hp'])
    print(p2['name'], p2['hp'])
    
    
    # TODO Select Skill DONE
    # TODO Solve Heal Attack function problem
    # TODO ADD cooldown to skills
    # TODO Add mana cost to skills
    
    break

if p1["hp"]>0:
    print(f"WINNER!! :P1 {p1['name']}")
else:
    print(f"WINNER!! :P2 {p2['name']}")
