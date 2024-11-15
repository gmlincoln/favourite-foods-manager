#Favourite Foods Manager App

favourite_foods = [] #Favourite Food List

while True: 
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View all favourite foods")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Thanks for using Favourite Foods Manager")
        break
    
    elif choice == "1":
        food = input("Enter a food name which you want to add: ")
        favourite_foods.append(food)
        print(f"{food} added successfully!")
    
    elif choice == "2":
        food = input("Enter a food name which you want to remove: ")
        favourite_foods.remove(food)
        print(f"{food} removed successfully!")
    
    elif choice == "3":
        if favourite_foods:
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food}")
        else:
            print("Your favourite food list is empty!")
            
        print("\n")

    else:
        print("Invalid choice!!!")