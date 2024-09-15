import tkinter as tk
from tkinter import ttk, messagebox
import requests 

API_KEY = ''
BASE_URL = "https://v6.exchangerate-api.com/v6/"

def get_exchange_rate(from_currency, to_currency):
    url = f"{BASE_URL}{API_KEY}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error while receiving data from API") 
    
    data = response.json()
    return data['conversion_rate']

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

def convert():
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    try:
        amount = float(amount_entry.get())
        result = convert_currency(amount, from_currency, to_currency)
        result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error!", "Please enter the correct amount!")
    except Exception as e:
        messagebox.showerror(f"An error occurred: {e}!")

root = tk.Tk()
root.title("Valute Converter")

tk.Label(root, text="Total: ").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From currency: ").grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "RUB"])
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
from_currency_combobox.set("USD")

tk.Label(root, text="In currency: ").grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "RUB"])
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
to_currency_combobox.set("EUR")

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()