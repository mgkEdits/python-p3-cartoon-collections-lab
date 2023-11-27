# Function to print out each dwarf name in number order
def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

# Function to capitalize each planeteer call and add an exclamation point
def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

# Function to check if any planeteer call is longer than four characters
def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

# Function to find and return the first string that is a type of cheese
def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in snacks:
        if item in cheeses:
            return item
    return None
