import random


class Game:
    def __init__(self):
        self.user_item = None
        self.computer_item = None

    def get_computer_item(self):
        choices = ["rock", "paper", "scisssors"]
        return random.choice(choices)
    
    def get_user_item(self):
        valid_choices = ['r', 'p', 's']
        mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        
        while True:
            choice = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            
            if choice in valid_choices:
                return mapping[choice]
            
            print("Invalid choice. Try again!")
    
    def get_game_result(self, user_item, computer_item):
        # Égalité
        if user_item == computer_item:
            return 'draw'
    
        # Le joueur gagne si :
        if user_item == 'rock' and computer_item == 'scissors':
            return 'win'
        if user_item == 'paper' and computer_item == 'rock':
            return 'win'
        if user_item == 'scissors' and computer_item == 'paper':
            return 'win'
    
        # Sinon il perd
        return 'loss'
    
    def play(self):
        # 1. Demander au joueur
        self.user_item = self.get_user_item()
        
        # 2. Ordinateur choisit
        self.computer_item = self.get_computer_item()
        
        # 3. Comparer
        result = self.get_game_result(self.user_item, self.computer_item)
        
        # 4. Afficher
        print(f"\nYou selected: {self.user_item}")
        print(f"Computer selected: {self.computer_item}")
        
        if result == 'win':
            print("You win!")
        elif result == 'loss':
            print("You lose!")
        else:
            print("It's a draw!")
        
        # 5. Retourner
        return result
    
if __name__ == "__main__":
   
    game = Game()
    result = game.play()
    print(f"\nResult: {result}")
    
    
 