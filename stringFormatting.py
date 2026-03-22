from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistr1 = "Jagmohan"
labour_mistr2 = "Rampyare"
is_home = True

if length_of_land == 100 : 
    length_of_land = 200
else :
    length_of_land = 300

print(length_of_land, bricks_cost_per_piece, labour_mistr1, is_home)
print("Length of land is", length_of_land)
print("My home is of 4BHK. \nLength of the total land is 100")
print('''My home is of 4BHK. Length of the total land is 100''')
print("My home is of '4BHK'")
print('My home is of "4BHK"')
print("My home is of \"4BHK\" ")