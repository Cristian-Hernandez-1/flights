import pandas as pd
import random as rd

movies_df = pd.read_csv('media_data/movies_cleaned.csv')
tvshows_df = pd.read_csv('media_data/tv_shows_cleaned.csv')

def movie(platform):
    movies_filtered_df = pd.DataFrame()
    if platform.lower() == "netflix":
        movies_filtered_df = movies_df[movies_df['netflix'] == 1]
    elif platform.lower() == "hulu":
        movies_filtered_df = movies_df[movies_df['hulu'] == 1]
    elif platform.lower() == "prime video":
        movies_filtered_df = movies_df[movies_df['prime_video'] == 1]
    elif platform.lower() == "disney+":
        movies_filtered_df = movies_df[movies_df['disney'] == 1]
    else:
        print("That platform doesn't exist to me! No offense " + platform)
        quit() 

    row_count = len(movies_filtered_df)
    random_number = rd.randint(1, row_count)
    choice = movies_filtered_df.iloc[random_number]['title']
    return choice

def tv_show(platform):
    tvshows_filtered_df = pd.DataFrame()
    if platform.lower() == "netflix":
        tvshows_filtered_df = tvshows_df[tvshows_df['netflix'] == 1]
    elif platform.lower() == "hulu":
        tvshows_filtered_df = tvshows_df[tvshows_df['hulu'] == 1]
    elif platform.lower() == "prime video":
        tvshows_filtered_df = tvshows_df[tvshows_df['prime_video'] == 1]
    elif platform.lower() == "disney+":
        tvshows_filtered_df = tvshows_df[tvshows_df['disney'] == 1]
    else:
        print("That platform doesn't exist to me! No offense " + platform)
        quit() 

    row_count = len(tvshows_filtered_df)
    random_number = rd.randint(1, row_count)
    choice = tvshows_filtered_df.iloc[random_number]['title']
    return choice
    

mood = input("whats the vibe today movie or tv show?\n")

if str(mood.lower()) == "movie" or str(mood.lower()) == "tv show":
    platform = input("what streaming platform (Netflix, Hulu, Prime Video, Disney+)\n")

    if str(mood.lower()) == "movie":
        movie_choice = movie(platform)
        print("Your random movie to watch is: " + '"' + movie_choice + '"')

    elif str(mood.lower()) == "tv show":
        tvshow_choice = tv_show(platform)
        print("Your random tv show to watch is: " + '"' + tvshow_choice + '"')

    else:
        print("I haven't heard of that streaming platform")
        quit()
else: 
    print("I have No clue what " + mood + " is? Quit messing with me!")
    quit()

 
