def roll_call_dwarves(list):
    i = 1
    for name in list:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planeteer_calls):
    return [f'{call.capitalize()}!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True

    return False

def find_the_cheese(foods):
    for food in foods:
        if food in ["camembert", "gouda", "cheddar"]:
            return food
    
    return None
