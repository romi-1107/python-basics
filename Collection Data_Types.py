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
inx           = backpack.index('Sword')
backpack[inx] = 'Magic GreatSword'
print('🚨', backpack)
print('-'*50)

print('4. 🔎Checking backpack')
print('🚨', backpack)

total_count  = len(backpack)
unique_items = set(backpack)
unique_count = len(unique_items)
potion_count = backpack.count('Potion')

print(f'There are {total_count} Items in Total')
print(f'There are {unique_count}Unique Items')
print(f'There are {potion_count} Potions')
print('-'*50)

print('5.🙃Dropped the Backpack Upside-Down ... ')
backpack.reverse()
print('🚨', backpack)
print('-'* 50)

print('6. ➡Sorting Items')
backpack.sort()

print('🚨', backpack)
print('-'* 50)

print('7. 💤Sleeping...')

a = backpack.pop()
b = backpack.pop(2)
c = backpack.pop()
stolen = [a,b,c]

print(f'Stolen: ',stolen)
print('🚨', backpack)
print('-'* 50)


print('8. 💍Found Magic Ring And Coin Pouch')
ring = 'Magic Ring'
coin_pouch = ['Gold Coin','Silver Coin']


backpack.insert(0,ring)
backpack.append(coin_pouch)

print('🚨', backpack)
print('-'* 50)

print('9. ✨Half Item Magically Disappeared. Damn You Magic Ring...')

count = len(backpack)
half = int(count / 2)
backpack = backpack[:half]

print('🚨',backpack)
print('-'* 50)

print('10. 👩‍🎓 Bandits Attack.')
print('Backpack Stolen...')

backpack = None
print('🚨', backpack)
print('-'* 50)


