import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window()
window.geometry("800x650")
window.title("Review User")

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 20))

great_review = ttk.Button(window,
                          text="😃 Great Review",
                          bootstyle="success",
                          width=50,
                          padding=20
                         )

good_review = ttk.Button(window,
                         text="🙂 Good Review",
                         bootstyle="info",
                         width=50,
                         padding=20)

regular_review = ttk.Button(window,
                            text="😐 Regular Review",
                            bootstyle="warning",
                            width=50,
                            padding=20)

bad_review = ttk.Button(window,
                        text="☹️ Bad Review",
                        bootstyle="danger",
                        width=50,
                        padding=20)


tittle = ttk.Label(window, text="Review User", font=("Helvetica", 34))

tittle.pack(pady=20)
great_review.pack(pady=10)
good_review.pack(pady=10)
regular_review.pack(pady=10)
bad_review.pack(pady=10)

window.mainloop()