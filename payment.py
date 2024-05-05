import tkinter as tk

def process_payment():
    print("Payment completed.")

def format_credit_card_number(e):
    s = e.get().replace("-", "")[:16]  
    formatted = '-'.join([s[i:i+4] for i in range(0, len(s), 4)])  
    e.delete(0, tk.END) 
    e.insert(0, formatted)  

def show_invoice():
    invoice_window = tk.Toplevel(root)
    invoice_window.title("Invoice")

    tk.Label(invoice_window, text="Billing Address", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(invoice_window, text=f"Full Name: {full_name_entry.get()}").pack()
    tk.Label(invoice_window, text=f"Email: {email_entry.get()}").pack()
    tk.Label(invoice_window, text=f"Address: {address_entry.get()}").pack()
    tk.Label(invoice_window, text=f"City: {city_entry.get()}").pack()
    tk.Label(invoice_window, text=f"State: {state_entry.get()}").pack()
    tk.Label(invoice_window, text=f"Zip: {zip_entry.get()}").pack()

    tk.Label(invoice_window, text="Payment", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(invoice_window, text=f"Accepted Cards: {card_var.get()}").pack()
    tk.Label(invoice_window, text=f"Credit Card Number: {credit_card_entry.get()}").pack()
    tk.Label(invoice_window, text=f"Exp Month: {exp_month_var.get()}").pack()
    tk.Label(invoice_window, text=f"CVV: {cvv_entry.get()}").pack()

root = tk.Tk()
root.title("Payment Form")

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

billing_frame = tk.LabelFrame(main_frame, text="Billing Address")
billing_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

tk.Label(billing_frame, text="Full Name:").grid(row=0, column=0, sticky="w")
full_name_entry = tk.Entry(billing_frame)
full_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(billing_frame, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(billing_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(billing_frame, text="Address:").grid(row=2, column=0, sticky="w")
address_entry = tk.Entry(billing_frame)
address_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(billing_frame, text="City:").grid(row=3, column=0, sticky="w")
city_entry = tk.Entry(billing_frame)
city_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(billing_frame, text="State:").grid(row=4, column=0, sticky="w")
state_entry = tk.Entry(billing_frame)
state_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(billing_frame, text="Zip:").grid(row=5, column=0, sticky="w")
zip_entry = tk.Entry(billing_frame)
zip_entry.grid(row=5, column=1, padx=5, pady=5)

payment_frame = tk.LabelFrame(main_frame, text="Payment")
payment_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

tk.Label(payment_frame, text="Accepted Cards").grid(row=0, column=0, sticky="w")
card_var = tk.StringVar()
card_var.set("VISA")  
card_dropdown = tk.OptionMenu(payment_frame, card_var, "VISA", "MASTER", "DEBIT")
card_dropdown.grid(row=0, column=1, padx=5, pady=5)

tk.Label(payment_frame, text="Name on Card:").grid(row=1, column=0, sticky="w")
tk.Entry(payment_frame).grid(row=1, column=1, padx=5, pady=5)

tk.Label(payment_frame, text="Credit card number:").grid(row=2, column=0, sticky="w")
credit_card_entry = tk.Entry(payment_frame)
credit_card_entry.grid(row=2, column=1, padx=5, pady=5)
credit_card_entry.bind("<KeyRelease>", lambda _: format_credit_card_number(credit_card_entry))

exp_frame = tk.Frame(payment_frame)
exp_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
tk.Label(exp_frame, text="Exp Month:").grid(row=0, column=0, sticky="w")
exp_month_var = tk.IntVar()
exp_month_var.set(1)
exp_month_entry = tk.Spinbox(exp_frame, from_=1, to=12, width=3, textvariable=exp_month_var)
exp_month_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(exp_frame, text="Exp Year:").grid(row=0, column=2, sticky="w")
tk.Entry(exp_frame, width=5).grid(row=0, column=3, padx=5, pady=5)

tk.Label(payment_frame, text="CVV:").grid(row=4, column=0, sticky="w")
cvv_entry = tk.Entry(payment_frame, width=5, show="*")  
cvv_entry.grid(row=4, column=1, padx=5, pady=5)
cvv_entry['validate'] = 'key'
cvv_entry['validatecommand'] = (root.register(lambda x: len(x) <= 3), '%P')  

checkout_button = tk.Button(main_frame, text="Continue to checkout", command=show_invoice)
checkout_button.grid(row=2, column=0, pady=10)

root.mainloop()
