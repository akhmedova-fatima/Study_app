import random
import re
import threading

users={}
def register():
    print("\n===register===")
    username=input("Enter your username: ")

    if username in users:
        print("username already taken")
        return

    password=input("Enter your password: ")
    if len(password)<5:
        print("password must be at least 5 characters long")
        return

    if not re.fullmatch(r"[A-za-z0-9]+", password):
        print("password must contain only english letters and numbers")
        return
    users[username]={"password":password, "cards":[], "notes": []}
    print("You successfully registered")
    user_menu(username)

def login():
    print("\n===login===")
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    if username in users and users[username]["password"]==password:
        print("login successful")
        user_menu(username)
    else:
        print("Incorrect username or password")

def add_card(username):
    print("\n===add card===")
    question=input("Enter your question: ")
    answer=input("Enter your answer: ")

    users[username]["cards"].append({"question":question,"answer":answer})
    print("You successfully added")

def review_random_card(username):
    cards=users[username]["cards"]

    if not cards:
        print("There are no cards")
        return

    card=random.choice(cards)

    print("\n===Repeating===")
    print("Question:",card["question"])
    input("Press Enter to see your answer...")
    print("Answer:",card["answer"])

def get_input(result):
    result.append(input("Enter your answer: "))

def start_quiz(username):
    cards=users[username]["cards"]
    if not cards:
        print("There are no cards")
        return

    print("\n===Quiz===")
    print("There are given 30 sec to each question")

    score=0
    random.shuffle(cards)

    for card in cards:
        print("\nQuestion:",card["question"])

        result = []
        thread = threading.Thread(target=get_input, args=(result,))
        thread.start()

        thread.join(timeout=30)

        if thread.is_alive():
            print("Time is over. Next question!")
            continue

        user_answer = result[0]


        if user_answer.lower()==card["answer"].lower():
            print("Correct!")
            score+=1
        else:
            print("Wrong!")
            print("Right answer:",card["answer"])

    print(f"\nQuiz is over. Your score is: {score}")

def add_note(username):
    print("\n===add note===")
    note=input("Enter your note: ")
    users[username]["notes"].append(note)
    print("Note is successfully added")

def view_note(username):
    print("\n===Your notes===")
    notes=users[username]["notes"]

    if not notes:
        print("There are no notes")
        return

    for i, note in enumerate(notes):
        print(f"{i}. {note}")

def edit_note(username):
    print("\n===Edit note===")
    view_note(username)
    notes=users[username]["notes"]

    if not notes:
        return

    index=int(input("Enter the number of note to edit: "))

    if 0<= index < len(notes):
        new_note=input("Enter the new note: ")
        notes[index]=new_note
        print("Note is successfully edited")
    else:
        print("Wrong index")

def delete_note(username):
    print("\n===Delete note===")
    view_note(username)
    notes=users[username]["notes"]

    if not notes:
        return

    index=int(input("Enter the number of note to delete: "))
    if 0<= index < len(notes):
        deleted=notes.pop(index)
        print("Note is successfully deleted")
    else:
        print("Wrong index")


def user_menu(username):
    while True:
        print(f"\n===User Menu===")
        print("1. Add card")
        print("2. Review random card")
        print("3. Launch the quiz")
        print("4. Add note")
        print("5. View notes")
        print("6. Edit note")
        print("7. Delete note")
        print("8. Exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_card(username)
        elif choice==2:
            review_random_card(username)
        elif choice==3:
            start_quiz(username)
        elif choice==4:
            add_note(username)
        elif choice==5:
            view_note(username)
        elif choice==6:
            edit_note(username)
        elif choice==7:
            delete_note(username)
        elif choice==8:
            print("Logout")
            break
        else:
            print("Wrong choice")

def main():
    while True:
        print("\n===Main Menu===")
        print("1.Registration")
        print("2.Login")
        print("3.Logout")

        choice=int(input("Enter your choice: "))
        if choice==1:
            register()
        elif choice==2:
            print("You are successfully logged in")
            login()
        elif choice==3:
            print("Thank for using this program")
            break
        else:
            print("Wrong choice")

main()