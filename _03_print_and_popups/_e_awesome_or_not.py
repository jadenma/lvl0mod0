from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your variable to the console
    print(num)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring(title='Awesome or not?', prompt="What is something that you think is awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if num == 0:
        messagebox.showinfo(title='Awesome!', message=awesome + " is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if num == 1:
        messagebox.showinfo(title='Okay.', message=awesome + " is okay.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if num == 2:
        messagebox.showinfo(title='Boring!', message=awesome + " is boring!")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if num == 3:
        messagebox.showinfo(title='Huh!', message=awesome + " is so boring that i don't know what it is!")
    # Run the window's .mainloop() method
    window.mainloop()
