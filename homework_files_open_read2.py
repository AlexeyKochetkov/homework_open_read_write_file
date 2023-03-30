
def get_shop_list_by_dishes(dishes, person_count):

    from pprint import pprint
    
    with open('recipes.txt', 'rt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            for dish in dishes:
                dish_name = line.strip()
                if dish == dish_name:
                    ingredient_count = int(f.readline())
                    ingredients = []
                    for ingredient in range(ingredient_count):
                        ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                        ingredients.append({
                            'ingredient_name': ingredient_name, 
                            'quantity': int(quantity) * person_count, 
                            'measure': measure
                        })
                    f.readline()
                    cook_book[dish_name] = ingredients

        
        ingredients = {}
        for dish_name in cook_book:
            ingredients2 = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity']} for ingredient in cook_book[dish_name]}  
            ingredients = {**ingredients, **ingredients2}

        pprint(ingredients) 

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)   