from game import Game

def get_user_menu_choice():
    print("\n" + "="*40)
    print("ROCK PAPER SCISSORS GAME")
    print("="*40)
    print("(p) Play a new game")
    print("(s) Show scores")
    print("(q) Quit")
    print("="*40)
    
    valid_choices = ['p', 's', 'q']
    
    while True:
        choice = input("\nEnter your choice: ").lower()
        
        if choice in valid_choices:
            return choice
        
        print("Invalid choice. Use 'p', 's', or 'q'.")

def print_results(results):
    print("\n" + "="*40)
    print("FINAL STATISTICS")
    print("="*40)
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("="*40)
    
    total_games = sum(results.values())
    if total_games > 0:
        win_rate = (results['win'] / total_games) * 100
        print(f"Win Rate: {win_rate:.1f}%")
        print(f"Total Games: {total_games}")
    else:
        print("No games played.")
    
    print("\nThank you for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == 'p':
            game = Game()
            result = game.play()
            results[result] += 1
        
        elif choice == 's':
            print("\n" + "="*40)
            print("CURRENT SCORES")
            print("="*40)
            print(f"Wins:   {results['win']}")
            print(f"Losses: {results['loss']}")
            print(f"Draws:  {results['draw']}")
            total = sum(results.values())
            if total > 0:
                win_rate = (results['win'] / total) * 100
                print(f"Win Rate: {win_rate:.1f}%")
        
        elif choice == 'q':
            print_results(results)
            break
        
main()