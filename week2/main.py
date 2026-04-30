from os import system, name
import menu

def clear_screen() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def run(mymenu: menu) -> None:
    
    while True:
        clear_screen()
        mymenu.draw_menu()
        selected = mymenu.get_input()
        
        if not mymenu.handle_response(selected):
            break

def main():
    thisdict = {
        1: "Select option 1.",
        2: "Select option 2.",
        0: "Exit"
    }
    
    myMenu = menu.MyMenu(thisdict)
       
    run(myMenu)
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()