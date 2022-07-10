import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
    """"Simple timer application using tkinter."""

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=0, column=1)

        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 20), width=10)
        self.clock.grid(row=1, column=1, stick="S")

        self.time_label = tk.Label(self, text="hour min sec", font=("Courier", 10), width=15)
        self.time_label.grid(row=2, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=3, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=3, column=1, sticky="NW")

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=3, column=3, sticky="NE")

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        """Calculates the time"""
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        """Checks if valid time entered and updates the timer"""
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        """Calculates the time to be displayed"""
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


if __name__ == "__main__":
    """Main loop which creates program."""
    root = tk.Tk()
    root.title("TIMER")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
# import tkinter as tk

# class TestApp(tk.Frame, object):
#     ''' When the player presses the button, the player and the enemy
#     chooses the numbers among 0 ... 10 randomly. If player >= enemy,
#     the player wins, otherwise the enemy wins.
#     If the player doesn't press the button in 2 seconds, the enemy wins.
#     '''
#     def __init__(self, parent, *args, **kwargs):
#         self.parent = parent

#         super(TestApp, self).__init__(self.parent, *args, **kwargs)

#         self.attack_player = 0
#         self.attack_enemy = 0
        
#         self.score_player = 0
#         self.score_enemy = 0

#         self.id_lose_timeout = None

#         self.button_play = tk.Button(
#             self,
#             text = 'Press in 2 seconds',
#             command = self.click)
#         self.label_attack = tk.Label(
#             self,
#             text = 'Attack - Player : %2d, Enemy : %2d' % (0, 0))
#         self.label_score = tk.Label(
#             self,
#             text = 'Score - Player : %2d, Enemy : %2d' % (0, 0))

#         self.button_play.pack()
#         self.label_attack.pack()
#         self.label_score.pack()

#         # first turn
#         self.set_timer()

#     def set_timer(self):
#         self.cancel_timer() # to prevent duplication
#         self.id_lose_timeout = self.after(2000, self.lose_timeout)

#     def cancel_timer(self):
#         if self.id_lose_timeout is not None:
#             self.after_cancel(self.id_lose_timeout)
#             self.id_lose_timeout = None

#     def click(self):
#         # stop the timer
#         self.cancel_timer()        

#         self.attack_player = random.randint(0, 10)
#         self.attack_enemy = random.randint(0, 10)

#         self.label_attack.config(
#             text = 'Attack - Player : %2d, Enemy : %2d'
#             % (self.attack_player, self.attack_enemy))

#         if self.attack_player >= self.attack_enemy:
#             self.win()
#         else:
#             self.lose()

#         # restart the timer
#         self.set_timer()

#     def win(self):
#         self.score_player += 1
        
#         self.label_score.config(
#             text = 'Score - Player : %2d, Enemy : %2d'
#             % (self.score_player, self.score_enemy))

#     def lose(self):
#         self.score_enemy += 1
        
#         self.label_score.config(
#             text = 'Score - Player : %2d, Enemy : %2d'
#             % (self.score_player, self.score_enemy))

#     def lose_timeout(self):
#         self.label_attack.config(
#             text = 'Timeout!')
#         self.lose()

#         # restart the timer
#         self.set_timer()
        

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = TestApp(root)
#     app.pack()
#     root.mainloop()
