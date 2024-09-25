import random
def get_voteless_combination(namen, choices):
    random_naam_1, random_naam_2 = random.choice(namen), random.choice(namen)
    if random_naam_1 != random_naam_2:
        for choice in choices:
            if choice['name1']==random_naam_1 and choice['name2']==random_naam_2:
                print('bestaat al',random_naam_1, random_naam_2)
                return get_voteless_combination(namen, choices)
            elif choice['name1']==random_naam_2 and choice['name2']==random_naam_1:
                print('bestaat al',random_naam_1, random_naam_2)
                return get_voteless_combination(namen, choices)
            else:
                return random_naam_1, random_naam_2    
    else:
        print('1 en 2 zijn gelijk')
        return get_voteless_combination(namen, choices)   
    
    
    
def update_elo(players_dict, name_1, name_2, score_1, k=30):
    rating_1, rating_2 = players_dict[name_1], players_dict[name_2]
    
    expected_score_1 = 1 / (1 + 10 ** ((rating_2 - rating_1) / 400))
    expected_score_2 = 1 / (1 + 10 ** ((rating_1 - rating_2) / 400))
    
    new_rating_1 = rating_1 + k * (score_1 - expected_score_1)
    new_rating_2 = rating_2 + k * ((1 - score_1) - expected_score_2)
    
    players_dict[name_1], players_dict[name_2] = int(new_rating_1), int(new_rating_2)