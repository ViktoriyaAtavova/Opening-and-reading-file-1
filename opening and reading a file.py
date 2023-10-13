def cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        my_cook_book = {}
        for line in file.read().split('\n\n'):
            name = line.split('\n')[0]
            food_items = line.split('\n')[2:]
            cook_list = []
            for item in food_items:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, item.split(' | '))
                ingridients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                cook_list.append(ingridients)                                         
            my_cook_book.setdefault(name, cook_list)
    return my_cook_book     


def get_shop_list_by_dishes(dishes: list, person_count):
    buy_items = {}
    for meals in dishes:
        if meals in cook_book():
            food = cook_book().get(meals)
            for item in food:
                buy_list = list(item.values())
                ingridients = {'measure': buy_list[2], 'quantity': buy_list[1] * person_count}
                if buy_list[0] not in buy_items:
                    buy_items[buy_list[0]] = ingridients
                else:
                    buy_items[buy_list[0]] = {'measure': buy_list[2], 'quantity': buy_list[1] * person_count * 2}            
    return buy_items
  

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))