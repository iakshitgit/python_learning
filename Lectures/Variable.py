from loguru import logger

length = 100
breadth = 100

print("This is the output using the print method")
print(length, breadth)
print(id(length), id(breadth))

#There is another way. This is the accurate way to print the 
#output in python. 

#print the value of the variable
logger.info("This is output from the logger method")
logger.info(f"Length: {length}, Breadth: {breadth}")
#print the value of the id of the variable
logger.info(f"{id(length)}, {id(breadth)}")