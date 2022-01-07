characters = [
    {
        'name': 'Termite',
        'hp':100,
        'power':10,
        'special':20,
        'specialRoundLeft':3,
        'specialRoundCooldown':4
        
    },
    {
        'name': 'Volcano',
        'hp':500,
        'power':5,
        'special':20,
        'specialRoundLeft':5,
        'specialRoundCooldown':6
    },
    {
        'name': 'GlassCannon',
        'hp':50,
        'power':250,
        'special':20,
        'specialRoundLeft':4,
        'specialRoundCooldown':5
    }
]


print('Characters:')

for i,character in enumerate(characters):
    for key,value in character.items():   
        print(str(i)+" "+key,value, sep=' - ', end=' ')
    print()

p1=characters[int(input("p1 choose your character "))]
p2=characters[int(input("p1 choose your character "))]

print(f"p1 ={p1['name']}, p2={p2['name']}")

def attack(p,enemy):
   enemy["hp"]= enemy["hp"]-p["power"]
def special(p,enemy):
    enemy["hp"]= enemy["hp"]-p["special"]


while p1["hp"]>0 and p2["hp"]>0:
    

    if p1["specialRoundLeft"] ==1:
        special(p1,p2)
        print("p1 used special!!")
        p1["specialRoundLeft"]=p1["specialRoundCooldown"]
    else:    
        attack(p1,p2)
        print(f"p1 attacked!, p2 Hp :{p2['hp']}")
    p1["specialRoundLeft"]=p1["specialRoundLeft"]-1
    
   
    if p2["specialRoundLeft"] ==1:
        special(p2,p1)
        print("p2 used special!!")
        p2["specialRoundLeft"]=p2["specialRoundCooldown"]
    else:
        attack(p2,p1)  
        print(f"p2 attacked!, p1 Hp :{p1['hp']}")
    p2["specialRoundLeft"]=p2["specialRoundLeft"]-1

if p1["hp"]>0:
    print(f"WINNER!! :P1 {p1['name']}")
else:
    print(f"WINNER!! :P2 {p2['name']}")
