# <>=


karakterler = [
    {
        'isim': 'Termo',
        'hp':100,
        'power':10,
        'special':20,
        'specialRoundLeft':3,
        'specialRoundCooldown':4
        
    },
    {
        'isim': 'VOLKANNNN',
        'hp':500,
        'power':5,
        'special':20,
        'specialRoundLeft':5,
        'specialRoundCooldown':6
    },
    {
        'isim': 'AHHHH met',
        'hp':50,
        'power':250,
        'special':20,
        'specialRoundLeft':4,
        'specialRoundCooldown':5
    }
]


print('Karakterlerimiz:')

for i,karakter in enumerate(karakterler):
    for key,value in karakter.items():   
        print(str(i)+" "+key,value, sep=' - ', end=' ')
    print()

p1=karakterler[int(input("p1 karakter seç "))]
p2=karakterler[int(input("p1 karakter seç "))]

print(f"p1 ={p1['isim']}, p2={p2['isim']}")

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
        print(f"p1 saldırdı, p2 can :{p2['hp']}")
    p1["specialRoundLeft"]=p1["specialRoundLeft"]-1
    
   
    if p2["specialRoundLeft"] ==1:
        special(p2,p1)
        print("p2 used special!!")
        p2["specialRoundLeft"]=p2["specialRoundCooldown"]
    else:
        attack(p2,p1)  
        print(f"p2 saldırdı, p1 can :{p1['hp']}")
    p2["specialRoundLeft"]=p2["specialRoundLeft"]-1

if p1["hp"]>0:
    print(f"KAZANAN :P1 {p1['isim']}")
else:
    print(f"KAZANAN :P2 {p2['isim']}")
