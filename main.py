import tkinter as tk
from tkinter import ttk, font
 
 
# Define color options
colors = {
   "Black": "#000000", "Red": "#FF0000", "Green": "#00FF00", "Yellow": "#FFFF00",
   "Blue": "#0000FF", "Magenta": "#FF00FF", "Cyan": "#00FFFF", "White": "#FFFFFF"
}
backgrounds = colors.copy()  # Background colors use the same values
styles = ["Normal", "Bold", "Italic", "Bold/Italic"]
effects = ["None", "Underline"]
brightness_levels = ["Dim", "Normal", "Bright"]
 
 
class ColorTextApp(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Color Text App - The Pycodes")
       self.geometry("600x500")
       self.current_font = font.Font(family="Arial", size=12)  # Default font
       self.setup_ui()
 
 
   def setup_ui(self):
       self.text_entry = ttk.Entry(self, width=50)
       self.text_entry.grid(row=0, column=1, padx=10, pady=10)
 
 
       self.fore_color_var = tk.StringVar()
       ttk.Label(self, text="Foreground Color:").grid(row=1, column=0, padx=10, pady=5)
       self.fore_color_dropdown = ttk.Combobox(self, textvariable=self.fore_color_var, values=list(colors.keys()))
       self.fore_color_dropdown.grid(row=1, column=1, padx=10, pady=5)
 
 
       self.back_color_var = tk.StringVar()
       ttk.Label(self, text="Background Color:").grid(row=2, column=0, padx=10, pady=5)
       self.back_color_dropdown = ttk.Combobox(self, textvariable=self.back_color_var, values=list(backgrounds.keys()))
       self.back_color_dropdown.grid(row=2, column=1, padx=10, pady=5)
 
 
       self.style_var = tk.StringVar()
       ttk.Label(self, text="Text Style:").grid(row=3, column=0, padx=10, pady=5)
       self.style_dropdown = ttk.Combobox(self, textvariable=self.style_var, values=styles)
       self.style_dropdown.grid(row=3, column=1, padx=10, pady=5)
 
 
       self.effect_var = tk.StringVar()
       ttk.Label(self, text="Text Effect:").grid(row=4, column=0, padx=10, pady=5)
       self.effect_dropdown = ttk.Combobox(self, textvariable=self.effect_var, values=effects)
       self.effect_dropdown.grid(row=4, column=1, padx=10, pady=5)
 
 
       self.brightness_var = tk.StringVar()
       ttk.Label(self, text="Brightness:").grid(row=5, column=0, padx=10, pady=5)
       self.brightness_dropdown = ttk.Combobox(self, textvariable=self.brightness_var, values=brightness_levels)
       self.brightness_dropdown.grid(row=5, column=1, padx=10, pady=5)
 
 
       self.apply_btn = ttk.Button(self, text="Apply and Display", command=self.apply_colors)
       self.apply_btn.grid(row=6, column=1, padx=10, pady=10)
 
 
       # Using a Text widget to display the results instead of a Label
       self.display_text = tk.Text(self, height=10, width=50, font=self.current_font)
       self.display_text.grid(row=7, column=1, padx=10, pady=10)
 
 
   def apply_colors(self):
       text = self.text_entry.get()
       fore = colors.get(self.fore_color_var.get(), "#FFFFFF")
       back = backgrounds.get(self.back_color_var.get(), "#000000")
       style = self.style_var.get()
       effect = self.effect_var.get()
       brightness = self.brightness_var.get()
 
 
       # Update the font based on user input
       weight = "bold" if "Bold" in style else "normal"
       slant = "italic" if "Italic" in style else "roman"
       size = 10 if brightness == "Dim" else 14 if brightness == "Bright" else 12
 
 
       self.current_font.config(weight=weight, slant=slant, size=size)
       self.display_text.config(font=self.current_font, fg=fore, bg=back)
 
 
       # Clear existing text and insert new styled text
       self.display_text.delete('1.0', tk.END)
       self.display_text.insert(tk.END, text)
 
 
       # Apply underline if selected
       if effect == "Underline":
           self.display_text.tag_configure("underline", underline=True)
           self.display_text.tag_add("underline", "1.0", "end")
       else:
           self.display_text.tag_remove("underline", "1.0", "end")
 
 
if __name__ == "__main__":
   app = ColorTextApp()
   app.mainloop()
