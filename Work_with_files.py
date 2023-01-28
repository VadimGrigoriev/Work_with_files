from pprint import pprint

import os


def recipes(file):
    with open(file, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            food = line.strip()
            number = int(f.readline())
            ingredients = []
            for i in range(number):
                ingredient = f.readline().strip()
                product, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': product,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            cook_book[food] = ingredients
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    def add_dicts(dict_1, dict_2):
        for key in dict_1.keys():
            if key in dict_2.keys():
                dict_1[key]['quantity'] = dict_1[key]['quantity']\
                                          + dict_2[key]['quantity']
        return dict_1

    food = recipes('recipes.txt')
    result = {}

    for dish in dishes:
        for ing in food.get(dish):
            new_dict = {
                ing['ingredient_name']:
                    {'measure': ing['measure'],
                     'quantity': int(ing['quantity']) * person_count}
            }
            if ing['ingredient_name'] not in result:
                result.update(new_dict)
            else:
                add_dicts(result, new_dict)
    return result


def unification(directory):
    list_of_files = os.listdir(directory)
    res = {}
    for file in list_of_files:
        full_path = os.path.join(os.getcwd(), directory, file)
        with open(full_path, encoding='utf-8') as f:
            content = f.read()
            f.seek(0)
            len_file = len(f.readlines())
            my_dict = {os.path.basename(f.name): [len_file, content]}
            res.update(my_dict)
    sort_res = sorted(res, key=res.get)
    with open('result.txt', 'w', encoding='utf-8') as f:
        for k in sort_res:
            f.write('\n'.join([k, str(res[k][0]), res[k][1]]) + '\n')


# pprint(recipes('recipes.txt'), width=100, sort_dicts=False)

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)

unification('Text')
