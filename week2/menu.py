# This file is for blah blah blah
class MyMenu:
    def __init__(self, items: dict) -> None:
        self.menu_items = items
            
    def draw_menu(self) -> None:
        for item in self.menu_items:
            print(f"{item}. {self.menu_items[item]}")

    def get_input(self) -> int:
        choice = input("Choice: ")
        return int(choice)
    
    def get_menu_items(self) -> dict:
        return self.menu_items