
# 🍏 Food Ingredient Substituter AI

## 📌 Project Description
This project is an AI-powered tool that suggests **healthier alternatives** for ingredients. If an exact match isn't found, it uses **fuzzy string matching** to find the closest alternative.

## ✨ Features
- ✅ **Ingredient substitution** using a CSV dataset.
- 🧠 **AI-powered fuzzy matching** for similar ingredients.
- 📂 **CSV-based storage** for easy expansion.
- 🖥️ **Runs in VS Code** (future web version planned).

## 🛠️ Technologies Used
- **Python** (Core logic)
- **Pandas** (Handling CSV data)
- **FuzzyWuzzy** (AI-powered text matching)
- **Git & GitHub** (Version control)

## 🚀 Installation Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/joemsomi/Food-Ingredient-Substituter.git
   cd Food-Ingredient-Substituter
   ```
2. **Install dependencies**:
   ```bash
   pip install pandas fuzzywuzzy python-Levenshtein
   ```
3. **Run the script**:
   ```bash
   python main.py
   ```

## 🎯 How to Use
1. The script will ask you to **enter an ingredient**.
2. If a healthy alternative is found, it will be displayed.
3. If no exact match is found, AI will suggest the **closest ingredient**.
4. Type `exit` to stop the program.

### 📌 Example
```
Enter an ingredient you want to replace: margarine
Did you mean 'butter'? A healthier alternative is: avocado or olive oil
```

## 🔮 Future Improvements
- 🌍 Convert into a **web app** (Flask or Streamlit).
- ☁️ Deploy to **AWS** for online access.
- 📈 Expand the **ingredient database**.

## 📝 Contributing
Want to improve the project? Feel free to fork it and submit a pull request!

## 📧 Contact
- GitHub: [joemsomi](https://github.com/joemsomi)
- LinkedIn: [Joseph Msomi](https://www.linkedin.com/in/josephmsomi/)

🚀 **Let me know if you want any changes!**

