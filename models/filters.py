import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/processed/cleaned_df_02.csv")


# 1. Filter based on company
def filter_by_company(data, companies):
    """Returns items from the specified companies."""
    return data[data['company'].isin(companies)]


# 2. Filter based on calories
def filter_by_calories(data, min_calories, max_calories):
    """Returns items within the specified calorie range."""
    return data[(data['calories'] >= min_calories) & (data['calories'] <= max_calories)]


# 3. Filter based on protein
def filter_by_protein(data, min_protein, max_protein):
    """Returns items within the specified protein range."""
    return data[(data['protein'] >= min_protein) & (data['protein'] <= max_protein)]


# 4. Low-calorie filter
def low_calorie(data):
    """Returns items with less than 40 calories."""
    return data[data['calories'] < 40]


# 5. Low-fat filter
def low_fat(data):
    """Returns items with less than 3 grams of fat."""
    return data[data['total_fat'] < 3]


# 6. Low-sodium filter
def low_sodium(data):
    """Returns items with less than 140 milligrams of sodium."""
    return data[data['sodium'] < 140]


# 7. Low-carb filter
def low_carb(data):
    """Returns items with less than 9 grams of carbs."""
    return data[data['carbs'] < 9]


# 8. Low-fiber filter
def low_fiber(data):
    """Returns items with less than 0.5 grams of fiber."""
    return data[data['fiber'] < 0.5]


# 9. Low-sugar filter
def low_sugar(data):
    """Returns items with less than 5 grams of sugar."""
    return data[data['sugar'] < 5]


# 10. High-protein filter
def high_protein(data):
    """Returns items with more than 10 grams of protein."""
    return data[data['protein'] > 10]


# 11. Best for losing weight
def best_for_losing_weight(data):
    """Returns items that are low in calories and carbs but high in protein."""
    return data[(data['calories'] < 40) & (data['carbs'] < 9) & (data['protein'] > 10)]
