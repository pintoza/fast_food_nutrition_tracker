import streamlit as st
import pandas as pd
import numpy as np
from models.filters import (
    filter_by_company,
    filter_by_calories,
    filter_by_protein,
    low_calorie,
    low_fat,
    low_sodium,
    low_carb,
    low_fiber,
    low_sugar,
    high_protein,
    best_for_losing_weight
)


def main():

    @st.cache_resource  # This will cache the data loading to make the app faster
    def load_data():
        return pd.read_csv('data/processed/cleaned_df_02.csv')

    df = load_data().round()

    st.title("Fast Food Nutrition Calculator")

    st.write("This app will calculate the nutrition of your next fast food meal. You can find the source code [here](https://github.com/pintoza/fast_food_nutrition_tracker)")

    st.sidebar.title("Set Your Preferences")

    companies = df['company'].unique().tolist()
    selected_companies = st.sidebar.multiselect('Select Companies',
                                                companies,
                                                default=companies)

    min_calories = int(np.nanmin(df['calories']))
    max_calories = int(np.nanmax(df['calories']))
    selected_calories = st.sidebar.slider('Calories',
                                          min_value=min_calories,
                                          max_value=max_calories,
                                          value=(min_calories, max_calories))

    min_protein = int(np.nanmin(df['protein']))
    max_protein = int(np.nanmax(df['protein']))
    selected_protein = st.sidebar.slider('Protein (g)',
                                         min_value=min_protein,
                                         max_value=max_protein,
                                         value=(min_protein, max_protein))

    low_cal_option = st.sidebar.checkbox('Low Calories')
    low_fat_option = st.sidebar.checkbox('Low Fat')
    low_sodium_option = st.sidebar.checkbox('Low Sodium')
    low_carb_option = st.sidebar.checkbox('Low Carb')
    low_fiber_option = st.sidebar.checkbox('Low Fiber')
    low_sugar_option = st.sidebar.checkbox('Low Sugar')
    high_protein_option = st.sidebar.checkbox('High Protein')
    weight_loss_option = st.sidebar.checkbox('Best for Losing Weight')

    # Use the filter functions here
    filtered_df = filter_by_company(df, selected_companies)

    filtered_df = filter_by_calories(filtered_df, *selected_calories)

    filtered_df = filter_by_protein(filtered_df, *selected_protein)

    # Dietary preferences
    if low_cal_option:
        filtered_df = low_calorie(filtered_df)
    if low_fat_option:
        filtered_df = low_fat(filtered_df)
    if low_sodium_option:
        filtered_df = low_sodium(filtered_df)
    if low_carb_option:
        filtered_df = low_carb(filtered_df)
    if low_fiber_option:
        filtered_df = low_fiber(filtered_df)
    if low_sugar_option:
        filtered_df = low_sugar(filtered_df)
    if high_protein_option:
        filtered_df = high_protein(filtered_df)
    if weight_loss_option:
        filtered_df = best_for_losing_weight(filtered_df)

    if len(filtered_df) == 0:
        st.warning("No items match your preferences. Try adjusting the filters.")
    else:
        st.dataframe(filtered_df)

    st.write(f"Found {len(filtered_df)} items based on your preferences.")
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Click HERE to Download your Results!",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )


if __name__ == '__main__':
    main()
