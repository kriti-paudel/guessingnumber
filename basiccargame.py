command = ""
started = False

while True:
    command = input("< ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car started")

    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the car
''')
    elif command =="quit":
        print("It's over")
        break
    else:
        print("I don't understand")


