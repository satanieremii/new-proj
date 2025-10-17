def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter a value.")
            continue
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")

def yes_no(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s in ("y", "yes"):
            return True
        if s in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")

def main():
    name = input("Enter your name: ").strip()
    age = get_int("Enter your age: ")
    nationality = input("Enter your nationality: ").strip()

    if yes_no("Show info? (y/n): "):
        print("\nGeneral info:")
        print(f"Name: {name or 'N/A'}")
        print(f"Age: {age}")
        print(f"Nationality: {nationality or 'N/A'}")
    else:
        print("No Info.")

if __name__ == "__main__":
    main()
    #end of test.py