human_age = float(input("Enter the dog's age in human years: "))
if human_age <= 2:
    dog_age = human_age*10.5
else:
    dog_age = (2*10.5) + (human_age-2)*4
print(f"The dog's age in dog’s years is {dog_age} years.")