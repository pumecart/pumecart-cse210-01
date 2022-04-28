def main():
    player = current_player("")
    other_player = ""
    
    interface = create_interface()
    while not (winning_combo(interface) or get_tie_game(interface, winning_combo)):
        display_interface(interface)
        make_move(player, interface)
        player = current_player(player)
    display_interface(interface)
    print("Good game! Thanks for playing!")

def create_interface():
    interface = []
    for space in range(9):
        interface.append(space + 1)
    return interface

def display_interface(interface):
    print(f"{interface[0]} {interface[1]} {interface[2]}")
    print("-" "+" "-" "+" "-")
    print(f"{interface[3]} {interface[4]} {interface[5]}")
    print("-" "+" "-" "+" "-")
    print(f"{interface[6]} {interface[7]} {interface[8]}")

def current_player(current_player):
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"

def make_move(player, interface):
    space = int(input(f"{player}'s turn to choose a square (1-9): "))
    interface[space - 1] = player

def winning_combo(interface):
    winning_combo = (interface[0] == interface[1] == interface[2] or
            interface[3] == interface[4] == interface[5] or
            interface[6] == interface[7] == interface[8] or
            interface[0] == interface[3] == interface[6] or
            interface[1] == interface[4] == interface[7] or
            interface[2] == interface[5] == interface[8] or
            interface[0] == interface[4] == interface[8] or
            interface[2] == interface[4] == interface[6])
    return winning_combo

def get_tie_game(interface, winning_combo):
    if not winning_combo:
        print ("It's a tie!  Play again for a tie breaker!")

if __name__ == "__main__":
    main()
