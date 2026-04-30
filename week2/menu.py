# This file is for blah blah blah
from time import sleep

class MyMenu:
    def __init__(self, items: dict) -> None:
        self.menu_items = items
            
    def draw_menu(self) -> None:
        for item in self.menu_items:
            print(f"{item}. {self.menu_items[item]}")

    def get_input(self) -> int:
        choice = input("Choice: ")
        return int(choice)
    
    def handle_response(self, choice: int) -> bool:
        match choice:
            case 0:
                print("Terminating program...")
                return False
            case 1 | 2:
                print("\n")
                print(self.menu_items[choice])
                print("\n")
                sleep(2)

        # it is a bit quick, so the resulkt is not visible long enough
        _ = input()
        return True