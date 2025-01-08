import json
import futhark_lib

def print_menu():
    print('1. Younger Futhark')
    print('2. Elder Futhark')
    print('3. Exit')

# Main function
def main():
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            data = futhark_lib.get_younger_futhark_json()
            print(json.dumps(data, indent=4))
        elif choice == '2':
            data = futhark_lib.get_elder_futhark_json()
            print(json.dumps(data, indent=4))
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
