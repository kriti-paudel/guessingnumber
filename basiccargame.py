command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car is start....")
    elif command == "stop":
        print("Car is stop...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - game over
""")
    elif command == "quit":
        print ("game over")
        break
    else:
        print("I don't understand")


