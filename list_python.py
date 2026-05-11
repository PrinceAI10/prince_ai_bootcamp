foods = []
for i in range(3):
    food = input(f"What is your favorite food {i+1}?: ")
    foods.append(food)
print(f"Your foods: {foods} ")
print(f"First food: {foods[0]} ")
print(f" You have {len(foods)} foods listed as your favorite in the meal plan. Congratulations! ")
