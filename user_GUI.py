import tkinter as tk
import ttkbootstrap as ttk

def change_window():
    review.destroy()
    satisfaction.deiconify()

review = ttk.Window()
review.geometry('800x600')
review.title("Review User")

satisfaction = ttk.Window()
satisfaction.geometry("800x650")
satisfaction.title("Review User")

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 20))

great_review = ttk.Button(satisfaction,
                          text="😃      Great",
                          bootstyle="success",
                          width=50,
                          padding=20
                         )

good_review = ttk.Button(satisfaction,
                         text="🙂       Good",
                         bootstyle="info",
                         width=50,
                         padding=20,
                         command=change_window)

regular_review = ttk.Button(satisfaction,
                            text="😐    Regular",
                            bootstyle="warning",
                            width=50,
                            padding=20,
                            command=change_window)

bad_review = ttk.Button(satisfaction,
                        text="😖      Bad",
                        bootstyle="danger",
                        width=50,
                        padding=20,
                        command=change_window)


tittle = ttk.Label(satisfaction, text="Deixe aqui a sua avaliação!", font=("Helvetica", 34))

tittle.pack(pady=20)
great_review.pack(pady=10)
good_review.pack(pady=10)
regular_review.pack(pady=10)
bad_review.pack(pady=10)

satisfaction.style.configure('success.TButton', font=(None, 25))
satisfaction.style.configure('info.TButton', font=(None, 25))
satisfaction.style.configure('warning.TButton', font=(None, 25))
satisfaction.style.configure('danger.TButton', font=(None, 25))
satisfaction.mainloop()