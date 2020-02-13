from test_data import *
import json


### Begin Add Code Here ###
#Loop through the json_data
    #Create a new Game object from the json_data by reading
    #  title
    #  year
    #  platform (which requires reading name and launch_year)
    #Add that Game object to the game_library
### End Add Code Here ###


#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = GameLibrary()
    for game in json_data:
        game_info = json_data[game]

        platform_info = game_info["platform"]
        title = game_info["title"]
        year = game_info["year"]

        p = Platform(platform_info["name"], platform_info["launch_year"])
        g = Game(title, p, year)
        game_library.add_game(g)
    return game_library



#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###

with open(input_json_file, "r") as reader:
    game_json_data = json.load(reader)

game_library = make_game_library_from_json(game_json_data)
print(game_library)
