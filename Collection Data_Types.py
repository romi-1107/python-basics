backpack = []
print('0.🙄Starting journey with empty backpack.')

print('🚨',backpack)
print('-'*50)

print('1.📦 Picking up Starterkit (Armor, Sheild, Sword, Potion).')
backpack.append('Armor')
backpack.append('Sheild')
backpack.append('Sword')
backpack.append('Potion')

print('🚨', backpack)
print('-'*50)

print('2.🎁 Looting a Treasure Chest!')
chest = ['Map', 'Potion', 'Compass', 'Potion']
print(f'Chest: {chest}')
backpack.extend(chest)

print('🚨', backpack)
print('-'*50)

print('3.🧙‍♂️ Visting Merchant')
print('-Selling the Sheild.')
print('- Upgrading Sword -> Magic GreatSword')

backpack.remove('Sheild')
inx = backpack.index('Sword')
backpack[inx] = 'Magic GreatSword'
print('🚨', backpack)
print('-'*50)

print('4. 🔎Checking backpack')
print('🚨', backpack)

total_count = len(backpack)
unique_items = set(backpack)
unique_count = len(unique_items)
potion_count = backpack.count('Potion')

print(f'There are {total_count} Items in Total')
print(f'There are {unique_count}Unique Items')
print(f'There are {potion_count} Potions')
