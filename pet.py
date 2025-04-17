class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5  # Starting hunger level
        self.energy = 5  # Starting energy level
        self.happiness = 5  # Starting happiness level
        self.tricks = []  # List to store learned tricks
        self.sleeping = False  # Indicator if the pet is sleeping

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} is eating... 🍽️")
        else:
            print(f"{self.name} is not hungry! 😕")

    def sleep(self):
        # Set the pet's sleeping state.
        self.sleeping = True
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... 😴")

    def wake_up(self):
        # Method to wake the pet up (if needed).
        if self.sleeping:
            self.sleeping = False
            print(f"{self.name} wakes up refreshed!")
        else:
            print(f"{self.name} is already awake!")

    def play(self):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot play right now!")
        elif self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing... 🎾")
        else:
            print(f"{self.name} is too tired to play! 😴")

    def groom(self):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot be groomed right now!")
        else:
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is being groomed... ✂️")

    def bathe(self):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot take a bath right now!")
        elif self.energy >= 3:
            self.energy = max(0, self.energy - 3)
            self.happiness = min(10, self.happiness + 3)
            print(f"{self.name} is taking a bath... 🛁")
        else:
            print(f"{self.name} is too tired for a bath! 😴")

    def go_for_walk(self):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot go for a walk!")
        elif self.pet_type.lower() in ["dog", "cat"]:
            if self.energy >= 4:
                self.energy = max(0, self.energy - 4)
                self.happiness = min(10, self.happiness + 4)
                print(f"{self.name} is going for a walk... 🚶")
            else:
                print(f"{self.name} is too tired for a walk! 😴")
        else:
            print(f"{self.name} doesn't enjoy walks! 🚫")

    def play_with_toy(self):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot play with a toy!")
        elif self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 3)
            print(f"{self.name} is playing with a toy... 🧸")
        else:
            print(f"{self.name} is too tired to play with a toy! 😴")

    def get_status(self):
        mood = self.get_mood()
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness} {mood}")
        print(f"Tricks: {self.tricks}")
        print(f"Sleeping: {self.sleeping}")

    def train(self, trick):
        if self.sleeping:
            print(f"{self.name} is sleeping and cannot learn a new trick right now!")
        else:
            self.tricks.append(trick)
            print(f"{self.name} has learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_mood(self):
        if self.happiness < 4:
            return "😢"
        elif self.happiness < 7:
            return "😐"
        else:
            return "😄"

    def custom_action(self):
        # First, check if the pet is sleeping.
        if self.sleeping:
            if self.pet_type.lower() == "dog":
                print(f"{self.name} is fast asleep, snoring softly like a happy dog. 💤🐕")
            elif self.pet_type.lower() == "cat":
                print(f"{self.name} is curled up in a sunny spot, snoozing contentedly. 💤🐱")
            elif self.pet_type.lower() == "rabbit":
                print(f"{self.name} is peacefully napping in its cozy hutch. 💤🐰")
            elif self.pet_type.lower() == "hamster":
                print(f"{self.name} is asleep in its little nest, dreaming away. 💤🐹")
            elif self.pet_type.lower() == "parrot":
                print(f"{self.name} is quietly resting on its perch. 💤🦜")
            elif self.pet_type.lower() == "fish":
                print(f"{self.name} is calmly floating in its aquarium, as if in a deep slumber. 💤🐠")
            else:
                print(f"{self.name} is sleeping peacefully. 💤")
            return

        # If the pet is awake, use the customized actions based on pet type, energy, and happiness.
        if self.pet_type.lower() == "dog":
            if self.happiness < 4:
                print(f"{self.name} looks sad and needs some playtime! 🐕")
            elif self.energy < 3:
                print(f"{self.name} is tired and wants to rest. 💤")
            else:
                print(f"{self.name} wags its tail and is ready for a walk! 🐶")

        elif self.pet_type.lower() == "cat":
            if self.happiness < 4:
                print(f"{self.name} is hiding and needs some attention! 🐱")
            elif self.energy < 3:
                print(f"{self.name} is napping and doesn't want to play. 😴")
            else:
                print(f"{self.name} is chasing a laser pointer! 🎯")

        elif self.pet_type.lower() == "rabbit":
            if self.happiness < 4:
                print(f"{self.name} looks a bit lonely and needs some cuddles! 🐰")
            elif self.energy < 3:
                print(f"{self.name} is resting in its cozy corner. 💤")
            else:
                print(f"{self.name} is hopping around happily! 🐇")

        elif self.pet_type.lower() == "hamster":
            if self.happiness < 4:
                print(f"{self.name} is sitting quietly and needs some playtime! 🐹")
            elif self.energy < 3:
                print(f"{self.name} is curled up in its bed, taking a nap. 😴")
            else:
                print(f"{self.name} is running on its wheel! 🏃")

        elif self.pet_type.lower() == "parrot":
            if self.happiness < 4:
                print(f"{self.name} is quiet and needs some interaction! 🦜")
            elif self.energy < 3:
                print(f"{self.name} is resting on its perch. 💤")
            else:
                print(f"{self.name} is singing a cheerful tune! 🎶")

        elif self.pet_type.lower() == "fish":
            if self.happiness < 4:
                print(f"{self.name} is swimming slowly and needs some attention! 🐠")
            elif self.energy < 3:
                print(f"{self.name} is resting at the bottom of the tank. 💤")
            else:
                print(f"{self.name} is swimming around happily! 🌊")

        else:
            print(f"{self.name} does something unique! 🦄")
            # custom action for unknown pet types