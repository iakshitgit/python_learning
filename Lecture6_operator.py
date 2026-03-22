from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

#Calculate the total area of the land
total_area_of_the_land = length_of_land*breadth_of_land
logger.info(f"Total area of the land is {total_area_of_the_land}")

#Calculate the perimeter of the land
perimeter_of_the_land = 2*(length_of_land+breadth_of_land)
logger.info(f"Perimeter of the land is {perimeter_of_the_land}")

#Modulo Operator
logger.info(15%6)

#Prints the Quotient
logger.info(15//6)

#Divide the number
logger.info(15/6)

#Floor
logger.info(math.floor(15/7))

#Ceiling
logger.info(math.ceil(15/7))