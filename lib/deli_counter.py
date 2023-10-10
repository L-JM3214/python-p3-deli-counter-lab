# deli_counter.py

katz_deli = []

def line(deli):
    if not deli:
        print("The line is currently empty.")
    else:
        positions = [f"{index + 1}. {person}" for index, person in enumerate(deli)]
        print("The line is currently: " + " ".join(positions))

def take_a_number(deli, person):
    deli.append(person)
    print(f"Welcome, {person}. You are number {len(deli)} in line.")

def now_serving(deli):
    if not deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli.pop(0)
        print(f"Currently serving {serving_person}.")

