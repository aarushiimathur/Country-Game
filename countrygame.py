import csv
import random

def openfile():
    rows = []
    with open("countrdb1.csv", 'r') as file:
        # This database has been collected from GIT itself and is not owned by me.
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    print(header)
    return rows

def countrycapitals(rows):
    while True:
        place = input("Enter the country whose capital you would like to know (type 'exit' to stop): ").strip()
        if place.lower() == 'exit':
            break
        found = 0
        for i in rows:
            country = i[0]
            capital = i[1]
            if place.lower() == country.lower():
                print("The capital is:", capital)
                found = 1
                break
        if found == 0:
            print("Country is not found on the list.")
        if __name__ == "__main__":
            main()

def knowcapitals(rows):
    while True:
        place = input("Enter the capital (type 'exit' to stop): ").strip()
        if place.lower() == 'exit':
            break
        found = 0
        for i in rows:
            country = i[0]
            capital = i[1]
            if place.lower() == capital.lower():
                print("The capital is:", country)
                found = 1
                break
        if found == 0:
            print("City is not found on the list.")
        if __name__ == "__main__":
            main()

def countrygame(rows):
    rrow = random.choice(rows)
    rcountry = rrow[0]
    rcapital = rrow[1]
    answer = input(f"What is the capital of {rcountry}? ").strip()

    if answer.lower() == rcapital.lower():
        print("Correct!!")
    else:
        print("Wrong!! The correct answer is:", rcapital)
    if __name__ == "__main__":
        main()

def capitals(rows):
    rrow = random.choice(rows)
    rcountry = rrow[0]
    rcapital = rrow[1]
    answer = input(f"Which country is {rcapital} the capital of? ").strip()

    if answer.lower() == rcountry.lower():
        print("Correct!!")
    else:
        print("Wrong!! The correct answer is:", rcountry)
    if __name__ == "__main__":
        main()
        

def main():
    print("Welcome!!!")
    choice = input("Would you like to \n 1. Country Game \n 2. Capital game\n 3. Know about countries\n 4. Know about the Capitals\n 5. Exit\n")

    rows = openfile()

    if choice == '1':
        print("You have decided to play the Country game.")
        countrygame(rows)
    elif choice == '2':
        print("You have decided to play the City game.")
        capitals(rows)
    elif choice == '3':
        print("Let's know about the capital of countries.")
        countrycapitals(rows)
    elif choice == '4':
        print("Lets find out which country the capital belongs to .")
        knowcapitals(rows)
    elif choice == '5':
        print("Thank you for playing")
        
    else:
        print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
