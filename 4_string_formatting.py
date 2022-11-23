## string formatting

first_name = 'Manguito'
print("Hi " + first_name)
print(f'Hi {first_name} this is Pollito!')

sentence = 'Hi {} {}'
last_name = 'Lovebird'
print(sentence.format(first_name, last_name))

print(f'Hi {first_name} {last_name} I hope you are chirping well')