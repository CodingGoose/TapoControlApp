import tkinter as tk
import plug_controller as pc

class CircularButton(tk.Canvas):
    def __init__(self, parent, icon_path, **kwargs):
        super().__init__(parent, width=100, height=100, **kwargs)
        
        # Draw a circle
        self.create_oval(10, 10, 90, 90, fill='lightblue', outline='black')
        
        # Load and add the icon
        self.icon = tk.PhotoImage(file=icon_path)
        self.create_image(50, 50, image=self.icon)
        
        # Bind mouse click event to the button
        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        print("Button clicked!")


#* MAIN APPLICATION WINDOW
window = tk.Tk()

window.geometry("300x500")
window.title("Tapo Control Center")

icon = tk.PhotoImage(file='.\\img\\icon.png') # makes icon.png into a so-called PhotoImage
window.iconphoto(True,icon)

window.config(background="#ffffff")

# # Circular button
# button = CircularButton(window, "./img/icon.png")
# button.pack(pady=20)

# On/Off button
button = tk.Button(window, text='On/Off')
button.config(command=pc.toggle_plug) #! you can either use config OR put all in the first Button() function
button.pack()

window.mainloop()