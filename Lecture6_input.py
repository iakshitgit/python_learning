from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

length_of_land = int(input("Enter the length of your land: "))
if length_of_land < 100:
    logger.info(f"Your length is not sufficient to build a 4BHK home.")
elif length_of_land > 500:
    logger.info(f"You can build more than 2 buildings.")
else :
    logger.info(f"Share more details with us")


