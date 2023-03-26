from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        ingredients = []
        for ingredient in range(ingredient_count):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name, 
                'quantity': quantity, 
                'measure': measure
            })
        f.readline()
        # print(dish_name)
        # pprint(ingredients)
        cook_book[dish_name] = ingredients
    pprint(cook_book, sort_dicts=False)