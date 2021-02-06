from usernames import build_profile as bd
def make_car(color, complectation, **info_car):
    information = {}
    information ['color_of_car=']= color
    information ['complectation_of_car=']= complectation
    for key, value in info_car.items():
        information [key]= value
    return information
car_information = make_car('red','none',model='BMW',
                             sit='4')
print(car_information)
    
