from Scrapper import get_car_data, save_to_csv
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

last_data = []


def display_data(car):
    global last_data
    data = get_car_data(car)
    last_data = data
    text_area.delete(1.0, tk.END)  # Clear previous data
    for item in data:
        text_area.insert(tk.END, f"Name: {item['name']}, Price: {item['price']}\n")


def save_data():
    if not last_data:
        messagebox.showwarning("No Data", "Please find prices before saving.")
        return
    filename = f"{dropdrown.get()}_prices.csv"
    save_to_csv(last_data, filename)
    messagebox.showinfo("Saved", f"Data saved to {filename}")


root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("600x400")


cars = ['kia', 'honda', 'toyota', 'suzuki', 'hyundai']

dropdrown = ttk.Combobox(root, values=cars)
dropdrown.current(3)
dropdrown.pack(pady=20)

find = tk.Button(root, text="Find Price", command=lambda: display_data(dropdrown.get()))
find.pack(pady=10)

save_btn = tk.Button(root, text="Save to CSV", command=save_data)
save_btn.pack(pady=10)

text_area = tk.Text(root, height=15, width=70)
text_area.pack(pady=20)


root.mainloop()