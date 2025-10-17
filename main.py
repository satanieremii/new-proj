def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter a value.")
            continue
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid information.")

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
    city = input("Enter your place of residency: ").strip()

    if yes_no("Show info? (y/n): "):
        print("\nGeneral info:")
        print(f"Name: {name or 'N/A'}")
        print(f"Age: {age}")
        print(f"City: {city or 'N/A'}")
    else:
        print("No Info.")

if __name__ == "__main__":
    main()
    #end of test.py