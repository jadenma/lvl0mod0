from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question1 = simpledialog.askstring(title='Question 1', prompt="What is 1+1?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question1 == str(2):
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question2 = simpledialog.askstring(title='Question 2', prompt="What is 2+2?")
    if question2 == str(4):
        score += 1
    question3 = simpledialog.askstring(title='Question 3', prompt="What is 3+3?")
    if question3 == str(6):
        score += 1
    question4 = simpledialog.askstring(title='Question 4', prompt="What is 4*4?")
    if question4 == str(16):
        score += 1
    question5 = simpledialog.askstring(title='Question 5', prompt="What is 5+5?")
    if question5 == str(10):
        score += 1
    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo(title='Quiz Results', message="Your score is: " + str(score))
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
