import pandas as pd 
import random as rd

movies_df = pd.read_csv('media_data/MoviesOnStreamingPlatforms.csv')
tvshows_df = pd.read_csv('media_data/tv_shows.csv')

movies_df = movies_df.drop_duplicates()
tvshows_df = tvshows_df.drop_duplicates()

movies_df.rename(columns={movies_df.columns[8]: 'Prime_Video'}, inplace=True)
tvshows_df.rename(columns={tvshows_df.columns[9]: 'Prime_Video'}, inplace=True)

movies_df.rename(columns={movies_df.columns[9]: 'Disney'}, inplace=True)
tvshows_df.rename(columns={tvshows_df.columns[10]: 'Disney'}, inplace=True)

def movie(platform):
    movies_filtered_df = pd.DataFrame()
    if platform.lower() == "netflix":
        movies_filtered_df = movies_df[movies_df['Netflix'] == 1]
    elif platform.lower() == "hulu":
        movies_filtered_df = movies_df[movies_df['Hulu'] == 1]
    elif platform.lower() == "prime video":
        movies_filtered_df = movies_df[movies_df['Prime_Video'] == 1]
    elif platform.lower() == "disney+":
        movies_filtered_df = movies_df[movies_df['Disney'] == 1]
    else:
        print("That platform doesn't exist to me! No offense " + platform)
        quit() 

    row_count = len(movies_filtered_df)
    # random_number = rd.randint(1, row_count)
    # choice = movies_filtered_df.iloc[random_number]['Title']
    return movies_filtered_df

def tv_show(platform):
    tvshows_filtered_df = pd.DataFrame()
    if platform.lower() == "netflix":
        tvshows_filtered_df = tvshows_df[tvshows_df['Netflix'] == 1]
    elif platform.lower() == "hulu":
        tvshows_filtered_df = tvshows_df[tvshows_df['Hulu'] == 1]
    elif platform.lower() == "prime video":
        tvshows_filtered_df = tvshows_df[tvshows_df['Prime_Video'] == 1]
    elif platform.lower() == "disney+":
        tvshows_filtered_df = tvshows_df[tvshows_df['Disney'] == 1]
    else:
        print("That platform doesn't exist to me! No offense " + platform)
        quit() 

    row_count = len(tvshows_filtered_df)
    # random_number = rd.randint(1, row_count)
    # choice = tvshows_filtered_df.iloc[random_number]['Title']
    return tvshows_filtered_df
    

print(movie("NETFLIX"))
print(tv_show("NETFLIX"))

# mood = input("whats the vibe today movie or tv show?\n")
# platform = input("what streaming platform (Netflix, Hulu, Prime Video, Disney+)\n")

# if str(mood.lower()) == "movie":
#     print(movie(platform))

# elif str(mood.lower()) == "tv show":
#     print(tv_show(platform))

# else:
#     print("No clue what " + mood + " is? Quit messing with me!")
#     quit()


 