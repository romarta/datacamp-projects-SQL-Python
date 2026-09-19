import pandas as pd
import matplotlib.pyplot as plt

workout = pd.read_csv("data/workout.csv")
three_keywords = pd.read_csv("data/three_keywords.csv")
workout_geo = pd.read_csv("data/workout_geo.csv")
three_keywords_geo = pd.read_csv("data/three_keywords_geo.csv")

# bes year for "workout"
max_month = workout.sort_values('workout_worldwide', ascending=False, ignore_index=True).head(1)
year_str = pd.to_datetime(max_month["month"].iloc[0]).strftime("%Y")
print(year_str)

# most popular keyword
covid_period = three_keywords[three_keywords["month"].between("2020-01", "2021-12")]
home_workout = covid_period['home_workout_worldwide'].mean()
gym_workout = covid_period['gym_workout_worldwide'].mean()
home_gym = covid_period['home_gym_worldwide'].mean()
print(home_workout, gym_workout, home_gym)
peak_covid = 'home_workout'

current_period = three_keywords[three_keywords["month"].str.startswith("2023")]
home_workout2 = current_period['home_workout_worldwide'].mean()
gym_workout2 = current_period['gym_workout_worldwide'].mean()
home_gym2 = current_period['home_gym_worldwide'].mean()
print(home_workout2, gym_workout2, home_gym2)
current = 'gym_workout'

#top cuntry
top = workout_geo.groupby('country')['workout_2018_2023'].mean().dropna().sort_values(ascending=False)
top_country = top.index[0]
print(top_country)

#home_workouts Philippines Malaysia
base = three_keywords_geo[['Country','home_workout_2018_2023']][three_keywords_geo["Country"].isin(['Philippines', 'Malaysia'])]
print(base.head())
home_workout_geo = 'Philippines'