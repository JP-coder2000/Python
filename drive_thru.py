foods = ["1.Cheeseburger", "2.Fries", "3.Soda", "4.Ice Cream", "5.Cookie"]

def welcome():
    print("Welcome to McDonalds drive through!")
    for food in foods:
        print(food)
    
def menu(choice):
    print(f"The food you selected: " + foods[choice - 1])

welcome()
menu(int(input("Please select the number of the food you'ld like: ")))
