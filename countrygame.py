import csv
import random

def openfile():
    rows = []
    with open("country-list.csv", 'r') as file:
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

def countrygame(rows):
    rrow = random.choice(rows)
    rcountry = rrow[0]
    rcapital = rrow[1]
    answer = input(f"What is the capital of {rcountry}? ").strip()

    if answer.lower() == rcapital.lower():
        print("Correct!!")
    else:
        print("Wrong!! The correct answer is:", rcapital)
        print("You can know about more countries and their capitals too")
        countrycapitals(rows)

def main():
    print("Welcome!!!")
    choice = input("Would you like to \n 1. Country Game \n 2. Know about countries \n")

    rows = openfile()

    if choice == '1':
        print("You have decided to play the Country game.")
        countrygame(rows)
    elif choice == '2':
        print("Let's know about the capital of countries.")
        countrycapitals(rows)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
