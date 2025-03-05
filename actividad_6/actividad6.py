import tkinter as tk
from tkinter import messagebox
import os

# Friend class to encapsulate friend details
class Friend:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}!{self.number}\n"

# FriendManager class to manage CRUD operations
class FriendManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()  # Create file if not exists

    def add_friend(self, friend: Friend):
        if self.read_friend(friend.name):
            return False  # Friend already exists
        with open(self.filename, 'a') as f:
            f.write(str(friend))
        return True

    def read_friend(self, name: str):
        with open(self.filename, 'r') as f:
            for line in f:
                friend_name, friend_number = line.strip().split("!")
                if friend_name == name:
                    return friend_number
        return None

    def update_friend(self, name: str, new_number: str):
        friends = self._load_friends()
        updated = False
        with open(self.filename, 'w') as f:
            for friend in friends:
                if friend.name == name:
                    friend.number = new_number
                    updated = True
                f.write(str(friend))
        return updated

    def delete_friend(self, name: str):
        friends = self._load_friends()
        new_friends = [friend for friend in friends if friend.name != name]
        if len(new_friends) == len(friends):  # No deletion happened
            return False
        with open(self.filename, 'w') as f:
            for friend in new_friends:
                f.write(str(friend))
        return True

    def _load_friends(self):
        """Helper method to load all friends from file."""
        friends = []
        with open(self.filename, 'r') as f:
            for line in f:
                if "!" in line:
                    name, number = line.strip().split("!")
                    friends.append(Friend(name, number))
        return friends

# Base GUI Class to avoid duplicate code
class BaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friend Manager")
        self.root.geometry("600x150")
        self.root.resizable(False, False)
        self.manager = FriendManager()
        self._create_widgets()

    def _create_widgets(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(expand=True)

        tk.Label(frame, text="Name:").grid(row=0, column=0, padx=20, pady=5)
        self.name_entry = tk.Entry(frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Number:").grid(row=1, column=0, padx=20)
        self.number_entry = tk.Entry(frame, width=30)
        self.number_entry.grid(row=1, column=1, pady=5)

        tk.Button(frame, text="Create", command=self.add_friend).grid(row=2, column=0, padx=7)
        tk.Button(frame, text="Read", command=self.get_friend).grid(row=2, column=1, padx=7)
        tk.Button(frame, text="Update", command=self.update_friend).grid(row=2, column=2, padx=7)
        tk.Button(frame, text="Delete", command=self.delete_friend).grid(row=2, column=3, padx=7)
        tk.Button(frame, text="Clear", command=self.clear_entries).grid(row=2, column=4, padx=7)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

# Main Application Class
class App(BaseGUI):
    def add_friend(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name and number:
            success = self.manager.add_friend(Friend(name, number))
            messagebox.showinfo("Success", "Friend added.") if success else messagebox.showwarning("Warning", "Friend already exists.")
        self.clear_entries()

    def get_friend(self):
        name = self.name_entry.get()
        if name:
            number = self.manager.read_friend(name)
            if number:
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, number)
            else:
                messagebox.showwarning("Warning", "Friend not found.")

    def update_friend(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name and number:
            success = self.manager.update_friend(name, number)
            messagebox.showinfo("Success", "Friend updated.") if success else messagebox.showwarning("Warning", "Friend not found.")
        self.clear_entries()

    def delete_friend(self):
        name = self.name_entry.get()
        if name:
            success = self.manager.delete_friend(name)
            messagebox.showinfo("Success", "Friend deleted.") if success else messagebox.showwarning("Warning", "Friend not found.")
        self.clear_entries()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
