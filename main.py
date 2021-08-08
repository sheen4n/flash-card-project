from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, width=800, height=700, pady=50, padx=50)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, fg="black")
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, fg="black")
right_button.grid(row=1, column=1)



window.mainloop()
