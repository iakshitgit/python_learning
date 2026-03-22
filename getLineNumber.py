from loguru import logger
import logging

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistr1 = "Jagmohan"
labour_mistr2 = "Rampyare"
is_home = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
)

logger.info(f"Cost of brick per unit is {bricks_cost_per_piece}")