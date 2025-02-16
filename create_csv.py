import pandas as pd

# Define the dataset
data = {
    "Ingredient": [
        "sugar", "butter", "margarine", "salt", "white flour", "cream",
        "mayonnaise", "vegetable oil", "sour cream", "white rice"
    ],
    "Healthier_Substitute": [
        "stevia or honey", "avocado or olive oil", "avocado or olive oil",
        "herbs or lemon juice", "almond flour or whole wheat flour",
        "Greek yogurt or coconut milk", "mashed avocado or Greek yogurt",
        "coconut oil or avocado oil", "Greek yogurt", "brown rice or quinoa"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save it as a CSV file
df.to_csv("healthy_substitutes.csv", index=False)

print("CSV file created successfully!")