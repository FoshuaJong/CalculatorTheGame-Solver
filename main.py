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

        button_choices = [add, sub, mul,
                          div, rem, ins,
                          rep, mypow, inv,
                          rev, mysum]
        buttons = []
        button_values = []
        selection = -1


        while True:
            print("\nCREATE BUTTONS\n"
                  "[1]Add      [2]Subtract    [3]Multiply\n"
                  "[4]Divide   [5]Remove      [6]Insert\n"
                  "[7]Replace  [8]Power       [9]Inverse\n"
                  "[10]Reverse [11]Sum\n"
                  "[0]Finish")

            try:
            selection = int(input("Selection: "))
            no_button_value = [5,9,10,11]

                if selection == 0:
                    break
                elif selection in no_button_value:
                    value = 0
                elif selection == 7:
                    old = int(input("Old: "))
                    new = int(input("New: "))
                    value = [old, new]
                else:
                    value = int(input("Button value: "))

                buttons.append(button_choices[selection - 1])
                button_values.append(value)
            except IndexError or ValueError:
                print("Oops, I didn't catch that, try again")

        solution = []
        attempts = 0
        threshold = 100000

        # Try to find a solution
        while number != goal and attempts<threshold:
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

        if number == goal:
            print("\n\nSolution Found")
            print("Total number of tries: {}".format(attempts))
            print("Original number: {}".format(start_value))
            for i in range(0,len(solution)):
                print("{}) {}".format(i+1, solution[i]))
            print("Number progression: {}".format(values))
        else:
            print("\nHmm, something went wrong. No solution was found after {} attempts.".format(threshold))
        keep_going = int(input("\nGo Again? [0]No [1]Yes\n"))




