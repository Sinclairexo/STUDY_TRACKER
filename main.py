import json
import random
study_session = []
motivations= [
    "DO NOT GIVE UP",
    "ALWAYS BE READY",
    "NO PAIN NO GAIN",
    "CONSISTENCY OVER PERFECTION",
    "KEEP GOING EVEN WHEN IT GETS HARD"
]
try:
    with open("study_session.json", "r") as f:
        study_session = json.load(f)
except FileNotFoundError:
    study_session = []
except json.decoder.JSONDecodeError:
    study_session = []
    print("Your study session file is empty or has been corrupted.")

while True:

    print("===================================")
    print("STUDY TRACKER")
    print("===================================")

    print("1. Add study session")
    print("2. View all sessions")
    print("3. View study statistics")
    print("4. Get random study motivation")
    print("5. Search sessions by subject")
    print("6. Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Enter a valid choice.")
        continue
    print(f"You chose {choice}")


    if choice == 1:
        name = input("Enter your name: ")
        sub_study = input("Enter the subject you're studying: ")

        while True:
            try:
                sub_minutes = int(input("Duration in Minutes: "))

                if sub_minutes > 0:
                    break
                else:
                    print("Duration in minutes must be greater than 0.")

            except ValueError:
                print("Enter a numeric value.")

        sub_learn = input("What did you learn?: ")

        study_session.append(
            {"name": name, "sub_study": sub_study, 'sub_minutes': sub_minutes, 'sub_learn': sub_learn})
        with open("study_session.json", "w") as f:
            json.dump(study_session, f, indent=4)
        print (study_session)
        print("Congrats, your session has been successfully added!")

        print("========= STUDY SESSION =========")
        print(f"Name: {name}")
        print(f"Subject: {sub_study}")
        print(f"Duration: {sub_minutes} minutes")
        print(f"Topic learned: {sub_learn}")

    elif choice == 2:
        if not study_session:
            print ("No study session found")
        else:
            print ("=============ALL STUDY SESSIONS =============")
            count = 1
            for session in study_session:
                print(f"\nSession {count}")

                for key, value in session.items():
                    print(f"{key}: {value}")

                print ("---------------------------------")
                count += 1

    elif choice == 3:
        if not study_session:
            print("You haven't recorded any study session yet")
        else:
            total_sessions = len(study_session)

            total_minutes = 0

            for session in study_session:
                total_minutes += session["sub_minutes"]


            total_hours = total_minutes / 60

            average_minutes = total_minutes / total_sessions

            print(f"Total sessions: {total_sessions} sessions")
            print (f"Total Study Time: {total_minutes} minutes")
            print (f"Total Study Time in Hours: {total_hours} hours")
            print (f"Average Session Duration: {average_minutes}")


    elif choice == 4:
        pick = random.choice(motivations)
        print (pick)

    elif choice == 5:
        subject = input("Enter the subject you're searching: ").lower()
        if not subject:
            print ("Please enter a subject")
        else:
            found = False
            for session in study_session:
                if subject in session["sub_study"].lower():
                    found = True
                    print ("\nYour subject has been found!")

                    for key, value in session.items():
                        print(f"{key}: {value}")
            if not found:
                print ("Subject not found")


    elif choice == 6:
        print("Thank you for using this program")
        break

    else:
        print("Invalid option, choose again")


