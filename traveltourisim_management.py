import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def create_files():
    try:
        pd.read_csv(r'C:\Users\Garv\OneDrive\Documents\users.csv')
    except FileNotFoundError:
        users_df = pd.DataFrame(columns=['username', 'password', 'email', 'phone'])
        users_df.to_csv('users.csv', index=False)
        users_df.to_excel('users.xlsx', index=False)
    try:
        pd.read_csv('bookings.csv')
    except FileNotFoundError:
        bookings_df = pd.DataFrame(columns=['id', 'username', 'package_name', 'booking_date'])
        bookings_df.to_csv('bookings.csv', index=False)
        bookings_df.to_excel('bookings.xlsx', index=False)


def register_user(username, password, email, phone):
    create_files()
    users_df = pd.read_csv(r'D:\Garv Tyagi XII I Material\users.csv')
    new_user = pd.DataFrame([[username, password, email, phone]], columns=['username', 'password', 'email', 'phone'])
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(r'C:\Users\Garv\OneDrive\Documents\users1.csv', index=False)
    users_df.to_excel(r'C:\Users\Garv\OneDrive\Documents\users1.xlsx', index=False)
    messagebox.showinfo("Success", "User registered successfully!")


def book_package(username, package_name, booking_date):
    create_files()
    bookings_df = pd.read_csv(r'D:\Garv Tyagi XII I Material\bookings.csv')
    new_booking = pd.DataFrame([[len(bookings_df) + 1, username, package_name, booking_date]], columns=['id', 'username', 'package_name', 'booking_date'])
    bookings_df = pd.concat([bookings_df, new_booking], ignore_index=True)
    bookings_df.to_csv(r'C:\Users\Garv\OneDrive\Documents\bookings1.csv', index=False)
    bookings_df.to_excel(r'C:\Users\Garv\OneDrive\Documents\bookings1.xlsx', index=False)
    messagebox.showinfo("Success", "Package booked successfully!")


def plot_bookings():
    def plot_bookings():
        create_files()
    bookings_df = pd.read_csv(r'D:\Garv Tyagi XII I Material\bookings.csv')
    if 'booking_date' not in bookings_df.columns:
        messagebox.showerror("Error", "'booking_date' column not found in bookings table")
        return
    bookings_df['booking_date'] = pd.to_datetime(bookings_df['booking_date'], errors='coerce')
    booking_counts = bookings_df.groupby(bookings_df['booking_date'].dt.date).size()

    plt.figure(figsize=(10, 5))
    booking_counts.plot(kind='bar')
    plt.title('Number of Bookings Over Time')
    plt.xlabel('Booking Date')
    plt.ylabel('Number of Bookings')
    plt.grid(0)
    plt.show()



def payment_window():
    window = tk.Toplevel()
    window.title("Payment")
    window.configure(bg='light blue')

    tk.Label(window, text="Username", font=("Helvetica", 14), bg='light blue').grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(window, font=("Helvetica", 14))
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Package Name", font=("Helvetica", 14), bg='light blue').grid(row=1, column=0, padx=10, pady=5)
    package_entry = tk.Entry(window, font=("Helvetica", 14))
    package_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Amount", font=("Helvetica", 14), bg='light blue').grid(row=2, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(window, font=("Helvetica", 14))
    amount_entry.grid(row=2, column=1, padx=10, pady=5)

    def process_payment():
        username = username_entry.get()
        package_name = package_entry.get()
        amount = amount_entry.get()
        if not username or not package_name or not amount:
            messagebox.showerror("Error", "All fields are mandatory!")
            return
        # Here you can add the logic to process the payment
        messagebox.showinfo("Success", "Payment processed successfully!")

    tk.Button(window, text="Process Payment", command=process_payment, font=("Helvetica", 14), bg='light blue').grid(row=3, columnspan=2, pady=10)


def create_main_window():
    root = tk.Tk()
    root.title("Travel and Tourism Management System")

    # Set background color
    root.configure(bg='light blue')

    # Create and place widgets
    tk.Label(root, text="Travel and Tourism Management System", font=("Helvetica", 16), bg='light blue').pack(pady=10)
    
    tk.Button(root, text="Register User", command=register_user_window, bg='light blue').pack(pady=5)
    tk.Button(root, text="Book Package", command=book_package_window, bg='light blue').pack(pady=5)
    tk.Button(root, text="Plot Bookings", command=plot_bookings, bg='light blue').pack(pady=5)
    tk.Button(root, text="Payment", command=payment_window, bg='light blue').pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, bg='light blue').pack(pady=5)

    root.mainloop()


def register_user_window():
    window = tk.Toplevel()
    window.title("Register User")
    window.configure(bg='light blue')

    tk.Label(window, text="Username", bg='light blue').grid(row=0, column=0)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    tk.Label(window, text="Password", bg='light blue').grid(row=1, column=0)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1)

    tk.Label(window, text="Email", bg='light blue').grid(row=2, column=0)
    email_entry = tk.Entry(window)
    email_entry.grid(row=2, column=1)

    tk.Label(window, text="Phone", bg='light blue').grid(row=3, column=0)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=3, column=1)

    tk.Button(window, text="Register", command=lambda: register_user(username_entry.get(), password_entry.get(), email_entry.get(), phone_entry.get()), bg='light blue').grid(row=4, columnspan=2, pady=10)


def book_package_window():
    window = tk.Toplevel()
    window.title("Book Package")
    window.configure(bg='light blue')

    tk.Label(window, text="Username", bg='light blue').grid(row=0, column=0)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)

    tk.Label(window, text="Package Name", bg='light blue').grid(row=1, column=0)
    package_name_entry = tk.Entry(window)
    package_name_entry.grid(row=1, column=1)

    tk.Label(window, text="Booking Date (YYYY-MM-DD)", bg='light blue').grid(row=2, column=0)
    booking_date_entry = tk.Entry(window)
    booking_date_entry.grid(row=2, column=1)

    tk.Button(window, text="Book", command=lambda: book_package(username_entry.get(), package_name_entry.get(), booking_date_entry.get()), bg='light blue').grid(row=3, columnspan=2, pady=10)

if __name__ == '__main__':
    create_main_window()
