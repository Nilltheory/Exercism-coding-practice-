"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below. 
def bake_time_remaining(time):
    """Calculate the bake time remaining.
    
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
    
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - time
    return bake_time_remaining
   
   



#TODO (student): Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(layers):
    """Calculate preparation time in minutes
        
    parameters:
        preparation_time_in_minutes (int): the amount of preparation time in minutes.
        number_of_layers (int): the number of layers added to the lasagna
    
    returns: 
        int: the preparation time (in minutes) derived from numner_of_layers.
    
    Define the preparation_time_in_minutes() function that takes the number_of_layers you want to add      to the lasagna as an argument and returns how many minutes you would spend making them. Assume         each layer takes 2 minutes to prepare.
    """
    PREPARATION_TIME = layers*(2)
    return PREPARATION_TIME
    
    
    
    
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time (prepping + baking) in minutes.
    
    parameters: 
        number_of_layers (int): the number of layers added to the lasagna
        elapsed_bake_time (int): the number of minutes the lasagna has spent baking in the oven already
    
    returns:
        int: the total time (in minutes) derived from elapsed_bake_time and number_of_layers
        
    This function should return the total minutes you have been in the kitchen cooking — your              preparation time layering + the time the lasagna has spent baking in the oven.
    """
    total_time = elapsed_bake_time + (number_of_layers*2)
    return total_time
    

   


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
