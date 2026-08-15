phonebook = {'Ricky : +43 4111 5111',
             'Tommy : +43 4222 6222',
             'Klaus : +43 4333 7333'}

phonebook['Erik']     = '+372 5555 5555'
phonebook['Kristina'] = '+372 5656 5656'
phonebook['Theo']     = '+372 5757 5757'

print(phonebook)


number = phonebook['Erik']
print(f'📞 Calling Erik...({number})')

number = phonebook['Theo']
print(f'📞 Calling Theo...({number})')

number = phonebook['kristina']
print(f'📞 Calling Kristina...({number})')
