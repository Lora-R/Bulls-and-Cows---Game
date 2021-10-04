from tkinter import *
import random

counter_list = []

def clear_view():
    # clear everything on the window
    for slave in tk.pack_slaves():
        slave.destroy()

def successfully_finish_game():
    global pop
    pop = Toplevel(tk)
    pop.title("You are the king of the farm")
    w = 450
    h = 500
    screen_w = pop.winfo_screenwidth()
    screen_h = pop.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)
    pop.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    pop.config(bg="Light green")
    pop_label = Label(pop, text="You guessed correct!")
    pop_label.pack(pady=30)
    pop_label.config(font=("Algerian", 15))

    pop = Canvas(pop, width=20, height=50)
    pop.pack()
    image_bull = PhotoImage(file="C:\\Users\\Me\\Desktop\\images_for_games\\bull_try.png")
    bull_l = Label(pop, image=image_bull)
    bull_l.photo = image_bull
    bull_l.pack()

    clear_view()

def not_successfully_finish_game(number_to_guess):
    global pop
    pop = Toplevel(tk)
    pop.title("You are the loser of the farm")
    w = 450
    h = 480
    screen_w = pop.winfo_screenwidth()
    screen_h = pop.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)
    pop.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    pop.config(bg="gray")
    pop_label = Label(pop, text=f"You waste your tries\n"
                                f"The correct number: {number_to_guess}\n"
                                f"Loser get out and try again")
    pop_label.pack(pady=30)
    pop_label.config(font=("Algerian", 15))

    pop = Canvas(pop, width=20, height=50)
    pop.pack()
    image_bull = PhotoImage(file="C:\\Users\\Me\\Desktop\\images_for_games\\cow-goat-family.png")
    bull_l = Label(pop, image=image_bull)
    bull_l.photo = image_bull
    bull_l.pack()
    clear_view()


def compare_numbers(list_guess_num, list_number_to_guess):
    # List where we will collect the amount of bulls and cows
    bull_cow_check = [0, 0]
    # Loop to check if any digit in your guess is the same as the correct one
    for i, i1 in zip(list_number_to_guess, list_guess_num):
        if i1 in list_number_to_guess:
            if i1 == i:
                bull_cow_check[0] += 1
            else:
                bull_cow_check[1] += 1

    # to get the number which we already entered, to save it(as label)
    num_guess = list(map(str, list_guess_num))
    num_guess_print = "".join(num_guess)

    # Label to show us how many are the bulls and the cows in our guess and also the our number
    label_bull_cow = Label(tk, text=f"{num_guess_print}\n "
                                    f"{bull_cow_check[0]} bulls, {bull_cow_check[1]} cows")
    label_bull_cow.pack(pady=5)
    # label_bull_cow.config(font=("Courier", 10))

    # check if the number that we guessed is the same as the one we are looking for
    if bull_cow_check[0] == 4:
        successfully_finish_game()

    # check for the amount of tries to guess
    if len(counter_list) == 8:
        number_to_guess = list(map(str, list_number_to_guess))
        number_to_guess = "".join(number_to_guess)
        not_successfully_finish_game(number_to_guess)

# To get the info from the entry box
def check_logic(entry_data, list_number_to_guess):
    # counter_list is to count the amount of tries, will be checked with len
    counter_list.append(1)

    num = entry_data.get()
    # putting the number in a list to compare it later
    list_guess_num = [int(n) for n in num]
    if len(list_guess_num) != 4:
        error_more_digits = Label(tk, text="The number can has 4 digit only. Please try again.")
        error_more_digits.pack(pady=10)
        # error_more_digits.config(font=("Courier", 10))
    else:
        if len(list_guess_num) != len(set(list_guess_num)):
            error_label = Label(tk, text="The number cannot have repeated digits. Please try again.")
            error_label.pack(pady=10)
            # error_label.config(font=("Courier", 10))
        else:
            print(list_guess_num)
            # Comparing the number(chosen randomly from the system) with the number(which we enter as a guess)
            compare_numbers(list_guess_num, list_number_to_guess)


def render_create_view(list_number_to_guess):
    clear_view()
    # Label for the beginning of the game
    lb = Label(tk, text="Let's the game begin!\n "
                        "Enter your guess")
    lb.pack(pady=20)
    lb.config(font=("Algerian", 20))

    # Entry data box, enter a number
    entry_data = Entry(tk, width=10, justify="center")
    entry_data.pack()

    # Submit button, which navigate us to "check logic function", to get the number writen into the Entry box
    submit_button = Button(tk, text="Submit", height=1, width=8, command=lambda: check_logic(entry_data, list_number_to_guess))
    submit_button.pack(pady=20)
    submit_button.config(font=("Algerian", 15))

def main_logic():
    # LOGIC/ number to guess, random number from the range 1000 - 9999
    while True:
        number_to_guess = random.randint(1000, 9999)
        # list_number_to_guess is a list with digits of the chosen number
        list_number_to_guess = [int(ng) for ng in str(number_to_guess)]
        # checking if the number has repeated digits
        if len(list_number_to_guess) == len(set(list_number_to_guess)):
            print(list_number_to_guess)
            render_create_view(list_number_to_guess)
            break


if __name__ == '__main__':
    # main visualization
    tk = Tk()
    tk.title("Bulls and Cows")
    w = 700
    h = 600
    screen_w = tk.winfo_screenwidth()
    screen_h = tk.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)
    tk.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

    # For the Start button// as image file
    tk = Canvas(tk, width=20, height=50)
    tk.pack()
    image = PhotoImage(file="C:\\Users\\Me\\Desktop\\images_for_games\\4nrgvh.png")

    start_button = Button(tk, image=image, height=320, width=520, command=main_logic)
    start_button.pack(pady=20)
    # explanation label for the game
    explanation = Label(tk, text="Welcome to the game 'Bulls and Cows'\n"
                                    "You need to guess a number, which is \n"
                                 "between 1000 and 10 000\n"
                                 "-|you have only 8 tries don't waste them|-\n"
                                    "If you are ready to smash the game, click\n"
                                 " on the Start button above")
    explanation.pack(pady=20)
    explanation.config(font=("Algerian", 20))

    # loop to keep the window visible
    tk.mainloop()