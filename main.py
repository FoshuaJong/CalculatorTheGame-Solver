from functions import *
import random as rand

if __name__ == '__main__':
    keep_going = 1

    while keep_going == 1:
        print("-------Solver for Calculator: The Game-------\n"
              "To leave at any point type a letter")
        moves = int(input("Moves: "))
        goal = int(input("Goal: "))
        start_value = int(input("Start Value: "))
        number = start_value

        button_choices = [add, sub, mul, div, rem, ins, rep]
        buttons = []
        button_values = []
        selection = -1

        while True:
            print("\nCREATE BUTTONS\n"
                  "[1]Add      [2]Subtract    [3]Multiply\n"
                  "[4]Divide   [5]Remove      [6]Insert\n"
                  "[7]Replace\n"
                  "[0]Finish")

            selection = int(input("Selection: "))

            if selection == 0:
                break
            elif selection == 5:
                value = 0
            elif selection == 7:
                old = int(input("Old: "))
                new = int(input("New: "))
                value = [old, new]
            else:
                value = int(input("Button value: "))

            buttons.append(button_choices[selection - 1])
            button_values.append(value)

        attempts = 0
        while number != goal:
            attempts += 1
            number = start_value
            solution = []
            values = []

            for i in range(0, moves):
                action = rand.randint(0,len(buttons)-1)

                number = int(float(number))
                number, text = call_function(number, buttons[action], button_values[action])
                if number % 1 != 0:
                    solution.append(text)
                    break

                solution.append(text)
                values.append(number)

            # debugging
            #print(number, solution)


        print("\n\nSolution Found")
        print("Original number: {}".format(start_value))
        for i in range(0,len(solution)):
            print("{}) {}".format(i+1, solution[i]))
        print("Number progression: {}".format(values))
        print("Total number of tries: {}".format(attempts))

        keep_going = int(input("\nKeep going? [0]No [1]Yes\n"))




