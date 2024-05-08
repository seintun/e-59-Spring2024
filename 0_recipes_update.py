import json
import uuid
import random

def update_ids(recipes):
    for recipe in recipes:
        # Update the RecipeID with a new UUID
        recipe["RecipeID"] = str(uuid.uuid4())

        for review in recipe["Reviews"]:
            review["UserID"] = str(random.randint(1, 150))
            review["Rating"] = round(random.uniform(0.5, 5.0) * 2) / 2

    return recipes

# Load the recipes
with open("recipes.json", "r") as f:
    recipes = json.load(f)

# Update the IDs
recipes = update_ids(recipes)

# Write the updated recipes back to the file
with open("recipes.json", "w") as f:
    json.dump(recipes, f, indent=2)