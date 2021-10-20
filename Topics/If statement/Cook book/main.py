pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredients = input()
# print(ingredients)
if ingredients in pasta:
    print("pasta time!")
if ingredients in apple_pie:
    print("apple pie time!")
if ingredients in ratatouille:
    print("ratatouille time!")
if ingredients in chocolate_cake:
    print("chocolate cake time!")
if ingredients in omelette:
    print("omelette time!")
