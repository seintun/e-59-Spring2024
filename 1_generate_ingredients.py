import json
import random
import string

def generate_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def generate_ingredients(names, calorie_range, allergens):
    ingredients = []
    for name in names:
        ingredient_id = generate_id()
        calorie_content = random.randint(calorie_range[0], calorie_range[1])
        allergen = random.choice(allergens)
        nutritional_facts = {
            "protein": f"{round(random.uniform(0, 30), 1)}g",
            "carbs": f"{round(random.uniform(0, 30), 1)}g",
            "fats": f"{round(random.uniform(0, 30), 1)}g",
            "fiber": f"{round(random.uniform(0, 10), 1)}g"
        }
        ingredient = {
            "ingredient_id": ingredient_id,
            "name": name,
            "calorie_content": calorie_content,
            "allergens": [allergen],
            "nutritional_facts": nutritional_facts
        }
        ingredients.append(ingredient)
    return ingredients

meats = ["Salmon", "Tuna", "Chicken breast", "Ground beef", "Bacon", "Pork ribs", "Shrimp", "Crab", "Lamb chops", "Venison", "Duck", "Turkey", "Beef steak", "Sausages", "Ham", "Sardines", "Trout", "Mussels", "Oysters", "Lobster"]
dairy = ["Whole milk", "Yogurt", "Cheese", "Butter", "Cream", "Sour cream", "Cottage cheese", "Whipped cream", "Margarine", "Condensed milk"]
eggs = ["Eggs", "Egg whites", "Egg yolks", "Quail eggs", "Duck eggs"]
vegetables = ["Spinach", "Kale", "Broccoli", "Carrots", "Tomatoes", "Avocado", "Bell peppers", "Eggplant", "Zucchini","Asparagus", "Lettuce", "Cabbage", "Cauliflower", "Brussels sprouts", "Artichoke", "Radish", "Celery", "Onion", "Garlic", "Ginger"]
fruits = ["Bananas", "Strawberries", "Blueberries", "Apples", "Oranges", "Grapes", "Pears", "Peaches", "Watermelon", "Cantaloupe", "Pineapple", "Mango", "Kiwi", "Lemon", "Lime", "Pomegranate", "Coconut", "Cherries", "Raspberries", "Blackberries"]
misc = ["Black beans", "Chickpeas", "Lentils", "Kidney beans", "Pinto beans", "White beans", "Soybeans", "Quinoa", "Brown rice", "Basmati rice", "Jasmine rice", "Barley", "Buckwheat", "Millet", "Oats", "Rye", "Farro", "Almonds", "Walnuts", "Cashews", "Peanuts", "Pistachios", "Hazelnuts", "Pecans", "Macadamia nuts", "Sunflower seeds", "Pumpkin seeds", "Chia seeds", "Flaxseeds", "Sesame seeds", "Hemp seeds", "Olive oil", "Coconut oil", "Avocado oil", "Canola oil", "Sesame oil", "Flaxseed oil", "Grapeseed oil", "Peanut oil", "Safflower oil", "Herbs de Provence", "Dill", "Thyme", "Cilantro", "Parsley", "Basil", "Oregano", "Sage", "Rosemary", "Mint", "Chives", "Tarragon"]


meat_ingredients = generate_ingredients(meats, (100, 600), ["none", "fish", "shellfish"])
dairy_ingredients = generate_ingredients(dairy, (50, 200), ["dairy"])
egg_ingredients = generate_ingredients(eggs, (100, 200), ["eggs"])
vegetable_ingredients = generate_ingredients(vegetables, (10, 50), ["none"])
fruit_ingredients = generate_ingredients(fruits, (10, 100), ["none"])
misc_ingredients = generate_ingredients(misc, (10, 50), ["none"])

all_ingredients = meat_ingredients + dairy_ingredients + egg_ingredients + vegetable_ingredients + fruit_ingredients + misc_ingredients

with open("ingredients.json", "w") as f:
    json.dump(all_ingredients, f, indent=2)
