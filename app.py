from flask import Flask, render_template

app = Flask(__name__)
# Dictionary of ingredient substitutions
ingredient_substitutes = {
    "butter": ["margarine", "applesauce", "yogurt"],
    "egg": ["flaxseed", "chia seeds", "applesauce"],
    "flour": ["almond flour", "coconut flour", "rice flour"],
    "milk": ["soy milk", "almond milk", "oat milk"]
}
# Home route (renders input form)

app.route('/')
def home():
    return render_template('home.html')

# Substitute route (handles form submission)
@app.route('/substitute', methods=['POST'])
def substitute():
    ingredient = request.form['ingredient'].lower()
    substitutes = ingredient_substitutes.get(ingredient, None)
    return render_template('substitutes.html', ingredient=ingredient, substitutes=substitutes)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    # Main Flask app

