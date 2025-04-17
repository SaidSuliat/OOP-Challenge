from pet import Pet

def main():
    # Interactive input for pet type
    print("Welcome to Hertz Pet Home! 🎉🐾")
    print("Available pet types: Dog 🐶, Cat 🐱, Rabbit 🐰, Hamster 🐹, Parrot 🦜, Fish 🐠")
    pet_type = input("What type of pet do you want? 🐾").strip().lower()
    
    # Determine the emoji based on the pet type
    pet_emojis = {
        "dog": "🐶",
        "cat": "🐱",
        "rabbit": "🐰",
        "hamster": "🐹",
        "parrot": "🦜",
        "fish": "🐠"
    }
    
    # Get the appropriate emoji or a default one if the type is not recognized
    pet_emoji = pet_emojis.get(pet_type, "🐾")  # Default to paw print if not recognized
    
    # Input for pet name with the corresponding emoji
    pet_name = input(f"Choose a cute name for your dear pet {pet_emoji}: ").strip()
    
    # Create a pet object
    my_pet = Pet(pet_name, pet_type)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet 🍽️")
        print("2. Put your pet to sleep 💤")
        print("3. Wake your pet up 🌞")
        print("4. Play with your pet 🎾")
        print("5. Groom your pet ✂️")
        print("6. Bathe your pet 🛁")
        print("7. Go for a Walk with your pet 🚶")
        print("8. Play with a Toy 🧸")
        print("9. Get Status 📊")
        print("10. Train a Trick 🎓")
        print("11. Show Tricks 🎉")
        print("12. Custom Action 🌟")
        print("13. Exit 👋")
        
        choice = input("Enter the number of your choice: ").strip()
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.wake_up()
        elif choice == '4':
            my_pet.play()
        elif choice == '5':
            my_pet.groom()
        elif choice == '6':
            my_pet.bathe()
        elif choice == '7':
            my_pet.go_for_walk()
        elif choice == '8':
            my_pet.play_with_toy()
        elif choice == '9':
            my_pet.get_status()
        elif choice == '10':
            trick = input("What trick do you want to teach your pet? ").strip()
            my_pet.train(trick)
        elif choice == '11':
            my_pet.show_tricks()
        elif choice == '12':
            my_pet.custom_action()
        elif choice == '13':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again. ❌")

if __name__ == "__main__":
    main()

# This code is a simple pet management game where users can interact with their virtual pet.
# Users can feed, groom, bathe, walk, play with their pet, and train it to learn tricks.