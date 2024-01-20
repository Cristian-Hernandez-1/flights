import pandas as pd

movies_df = pd.read_csv('media_data/MoviesOnStreamingPlatforms.csv')
tvshows_df = pd.read_csv('media_data/tv_shows.csv')

movies_df = movies_df.drop_duplicates()
tvshows_df = tvshows_df.drop_duplicates()

movies_df.rename(columns={movies_df.columns[8]: 'prime_video'}, inplace=True)
tvshows_df.rename(columns={tvshows_df.columns[9]: 'prime_video'}, inplace=True)

movies_df.rename(columns={movies_df.columns[5]: 'rotten_tomatoes'}, inplace=True)
tvshows_df.rename(columns={tvshows_df.columns[6]: 'rotten_tomatoes'}, inplace=True)

movies_df.rename(columns={movies_df.columns[9]: 'disney'}, inplace=True)
tvshows_df.rename(columns={tvshows_df.columns[10]: 'disney'}, inplace=True)

movies_df.columns = movies_df.columns.str.lower()
tvshows_df.columns = tvshows_df.columns.str.lower()

movies_df.drop(movies_df.columns[0], axis = 1, inplace=True)
tvshows_df.drop(tvshows_df.columns[0], axis = 1, inplace=True)

movies_df.to_csv('media_data/movies_cleaned.csv')
tvshows_df.to_csv('media_data/tv_shows_cleaned.csv')
