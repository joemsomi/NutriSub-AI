import pandas as pd
from fuzzywuzzy import process, fuzz

# Load the CSV file
df = pd.read_csv("healthy_substitutes.csv")

# Convert DataFrame to a dictionary
healthy_substitutes = dict(zip(df["Ingredient"], df["Healthier_Substitute"]))

def get_similar_ingredient(ingredient, ingredient_list):
    """Find the closest matching ingredient using fuzzy string matching."""
    match, score = process.extractOne(ingredient, ingredient_list, scorer=fuzz.token_sort_ratio)
    
    print(f"User input: {ingredient} → Closest match: {match} (Score: {score})")  # Debugging

    if score > 50:  # Lowered threshold for better matching
        return match
    return None  # No close match found

# Main program loop
def main():
    while True:
        ingredient = input("\nEnter an ingredient you want to replace (or type 'exit' to quit): ").lower()
        
        if ingredient == "exit":
            print("Goodbye! 👋")
            break
        
        if ingredient in healthy_substitutes:
            print(f"A healthier alternative for '{ingredient}' is: {healthy_substitutes[ingredient]}")
        else:
            similar_ingredient = get_similar_ingredient(ingredient, list(healthy_substitutes.keys()))
            
            if similar_ingredient:
                print(f"Did you mean '{similar_ingredient}'? A healthier alternative is: {healthy_substitutes[similar_ingredient]}")
            else:
                print("Sorry, no healthy substitute found for that ingredient.")

# Run the program
if __name__ == "__main__":
    main()