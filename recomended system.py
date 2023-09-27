import pandas as pd


# Sample movie dataset (Title, Genres, User Ratings)
data = {
    'Title': 
['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
   
 'Genres': ['Action', 'Comedy', 'Drama', 'Action', 'Comedy'],
    
'User_Rating': [4.5, 3.8, 4.0, 4.2, 3.5]
}


# Create a DataFrame from the dataset
df = pd.DataFrame(data)


# Function to recommend movies based on user preferences
def recommend_movies(user_genre_pref, num_recommendations=3):
   
 # Filter movies with matching genres
   
 matching_movies = df[df['Genres'].isin(user_genre_pref)]
    
   
 # Sort by user ratings in descending order
   
 sorted_movies = matching_movies.sort_values(by='User_Rating', ascending=False)
    
  
  # Get the top N recommended movies
  
  recommendations = sorted_movies.head(num_recommendations)
    
   
 return recommendations[['Title', 'Genres', 'User_Rating']]


# Sample user preferences
user_preferences = ['Action', 'Drama']


# Get movie recommendations for the user
recommendations = recommend_movies(user_preferences)


# Display recommended movies
print("Recommended Movies:")

print(recommendations)