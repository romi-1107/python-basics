player = {'Name'     : 'Erik',
          'Class'    : 'Warrior',
          'Health'   : 100,
          'Level'    : 1,
          'Backpack' : []
          }

player['Level'] += 1
print(player)

player['Backpack'].append('Item-A')
player['Backpack'].append('Item-B')
player['Backpack'].append('Item-C')
player['Backpack'].append([10,20,30])

for k,v in player.  items():
    print(k,v)