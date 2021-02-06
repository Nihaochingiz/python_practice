def show_magicians(names, great_names):
    while names:
        real_magician = names.pop()
        print ("Волшебник" + real_magician)
        great_names.append(real_magician)
def make_great(great_names):
    print("Великий волшебник:"+ great_names)
    for great_name in great_names:
        print (great_names)
    names = ['Николай','Владимир','Сергей','Артем',]
    great_names = []
    show_magicians(names, great_names)
    make_great(great_names)

  

        
    
        
    

    
    

