import json
import random
from faker import Faker

# Initialize the Faker library
fake = Faker()

def generate_user(user_id):
    return {
        "UserID": str(user_id),
        "Name": fake.name(),
        "Email": fake.email(),
        "Bio": fake.sentence(nb_words=15),
        "RecipesCreated": random.randint(1, 10)
    }

# Generate a list of users
users = [generate_user(user_id) for user_id in range(1, 151)]

# Write the users to a JSON file
with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

# Load the recipes
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Extract the recipe IDs
recipe_ids = [recipe["RecipeID"] for recipe in recipes]

# Assign recipes to each user
for user in users:
    user["Recipes"] = random.sample(recipe_ids, user["RecipesCreated"])

# Write the updated users back to the file
with open("users.json", "w") as f:
    json.dump(users, f, indent=2)