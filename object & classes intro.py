'''demonstrating how to use classes and objects'''
class Enemy:
    '''the enemy class has life, name and functions that do stuff'''
    
    def __init__(self, name, life):
        '''the init funcion runs on instantiation and sets up all the attributes'''
        self._name = name
        self._life = life
        #add the new enemy_list list
        enemy_list.append(self)
        
    def get_name(self):
        return self._name
    
    def get_life(self):
        '''this function returns the amount of life remaining'''
        return self._life
    
    def attack(self):
        '''this function subtracts 1 from the objects health'''
        self._life -= 1
        if self._life == 0:
            print("i ded")
        else:
            print("ow")

def show_all():
    '''This function displays the details of all enemies in the enemy list'''
    for enemy in enemy_list:
        print(enemy.get_name())
        
def life_check():
    life_input = int(input("Enter a value: "))
    for enemy in enemy_list:
        if enemy.get_life() >= life_input:
            print("{} has {} health left".format(enemy.get_name(), enemy.get_life()))
            
def create_enemy():
    '''this function allows the user to create a new enemy'''
    new_name = input("Enter a new name: ")
    new_life = int(input("Enter a new life value: "))
    Enemy(new_name, new_life)
# enemy_list stores all enemy objects
enemy_list = []

#create an enemy object and store in variable called enemy1
Enemy("personman", 5)
Enemy("otherpersonman", 100)
Enemy("otherotherpersonman", 50)

tf = True
while tf == True:
    print("1. show enemies")
    print("2. check enemy life")
    print("3. create new enemy")
    print("4. leave")
    user_choice = int(input())
    if user_choice == 1:
        show_all()
        input()
    elif user_choice == 2:
        life_check()
    elif user_choice == 3:
        create_enemy()
    else:
        tf = False