import json
import futhark_lib

def print_menu():
    print('1. Younger Futhark/JSON')
    print('2. Elder Futhark/JSON')
    print('3. Younger Futhark/DataFrame')
    print('4. Elder Futhark/DataFrame')
    print('5. Exit')

# Main function
def main():
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            data = futhark_lib.get_younger_futhark()
            print(json.dumps(data, indent=4))
        elif choice == '2':
            data = futhark_lib.get_elder_futhark()
            print(json.dumps(data, indent=4))
        elif choice == '3':
            df = futhark_lib.get_younger_futhark_df()
            print(df.to_string())
        elif choice == '4':
            df = futhark_lib.get_elder_futhark_df()
            print(df.to_string())
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()