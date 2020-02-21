import cc_dat_utils
import json
from cc_classes import *
from cc_dat_utils import *

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

# all maps are 32 x 32 grids
def make_CClevelpack_from_json_data(json_data):
    levelPack = CCLevelPack()

    for level in json_data:
        # Initialize the CCLevel object
        l = CCLevel()

        # Redefine the level properties for level_number, time, num_chips, and upper_layer
        l.level_number = level["level_number"]
        l.time = level["time"]
        l.num_chips = level["num_chips"]
        l.upper_layer = level["upper_layer"]
        
        # Define the optional fields list
        op_fields = []
        # Iterate through all the possible fields (title, password, hint, and monsters)
        for field in level["optional_fields"]:
            print(field)
            print(field["value"])
            if (field["field_type"] == "title"): # Add title field
                op_fields.append(CCMapTitleField(field["value"]))
            elif (field["field_type"] == "password"): # Add the password field
                op_fields.append(CCEncodedPasswordField(field["value"]))
            elif (field["field_type"] == "hint"): # Add the hint fiels
                op_fields.append(CCMapHintField(field["value"]))
            elif (field["field_type"] == "monster"): # Add the monsters field
                monsters = []
                # Iterate through all the possible monster coordinates to construct a monsters list
                for pos in field["value"]:
                    monsters.append(CCCoordinate(pos["x"], pos["y"]))
                op_fields.append(CCMonsterMovementField(monsters))
        
        l.optional_fields = op_fields
        
        levelPack.add_level(l)
    return levelPack

input_json_file = "data/mdunaevs_cc1.json"
with open(input_json_file, "r") as reader:
    game_json_data = json.load(reader)

levelPack = make_CClevelpack_from_json_data(game_json_data)
print(levelPack)

write_cc_level_pack_to_dat(levelPack, "data/mdunaevs_cc1.dat")