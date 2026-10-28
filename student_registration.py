import os
import csv
import re
import tkinter as tk
from tkinter import ttk, messagebox

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")


class StudentRegistrationApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("620x760")
        self.root.minsize(580, 700)
        self.root.configure(bg="#f1f5f9")

        # Initialize CSV file if not exists
        self.init_csv()

        # Build UI
        self.setup_styles()
        self.create_widgets()

    def init_csv(self) -> None:
        """Create CSV file with header if it doesn't exist."""
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Roll Number",
                    "Full Name",
                    "Email",
                    "Phone",
                    "Gender",
                    "Course",
                    "Date of Birth",
                    "Address"
                ])

    def setup_styles(self) -> None:
        """Configure modern ttk styles."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # General styling
        self.style.configure(".", font=("Segoe UI", 10))
        self.style.configure("TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), foreground="#1e293b", background="#ffffff")
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 9), foreground="#64748b", background="#ffffff")

        # Button styling
        self.style.configure(
            "Primary.TButton",
            font=("Segoe UI", 10, "bold"),
            background="#2563eb",
            foreground="#ffffff",
            padding=(12, 8),
            borderwidth=0
        )
        self.style.map("Primary.TButton", background=[("active", "#1d4ed8")])

        self.style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10),
            background="#e2e8f0",
            foreground="#1e293b",
            padding=(10, 8),
            borderwidth=0
        )
        self.style.map("Secondary.TButton", background=[("active", "#cbd5e1")])

        self.style.configure(
            "Outline.TButton",
            font=("Segoe UI", 10),
            background="#ffffff",
            foreground="#2563eb",
            padding=(10, 8),
            borderwidth=1
        )

    def create_widgets(self) -> None:
        """Create and lay out all window components."""
        # Main container with a clean card appearance
        card = tk.Frame(self.root, bg="#ffffff", bd=1, relief=tk.SOLID)
        card.pack(fill=tk.BOTH, expand=True, padx=24, pady=24)

        # Header section
        header_frame = tk.Frame(card, bg="#ffffff")
        header_frame.pack(fill=tk.X, padx=24, pady=(20, 10))

        ttk.Label(
            header_frame,
            text="Student Registration Form",
            style="Header.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header_frame,
            text="Please fill in all the details below to register a new student.",
            style="SubHeader.TLabel"
        ).pack(anchor="w", pady=(2, 0))

        # Divider line
        divider = tk.Frame(card, height=1, bg="#e2e8f0")
        divider.pack(fill=tk.X, padx=24, pady=(10, 15))

        # Form fields container
        form_frame = tk.Frame(card, bg="#ffffff")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=5)
        form_frame.columnconfigure(1, weight=1)

        row = 0

        # Roll Number / Student ID
        ttk.Label(form_frame, text="Roll Number / ID *").grid(row=row, column=0, sticky="w", pady=6)
        self.roll_entry = ttk.Entry(form_frame, font=("Segoe UI", 10))
        self.roll_entry.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Full Name
        ttk.Label(form_frame, text="Full Name *").grid(row=row, column=0, sticky="w", pady=6)
        self.name_entry = ttk.Entry(form_frame, font=("Segoe UI", 10))
        self.name_entry.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Email
        ttk.Label(form_frame, text="Email Address *").grid(row=row, column=0, sticky="w", pady=6)
        self.email_entry = ttk.Entry(form_frame, font=("Segoe UI", 10))
        self.email_entry.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Phone Number
        ttk.Label(form_frame, text="Phone Number *").grid(row=row, column=0, sticky="w", pady=6)
        self.phone_entry = ttk.Entry(form_frame, font=("Segoe UI", 10))
        self.phone_entry.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Gender
        ttk.Label(form_frame, text="Gender *").grid(row=row, column=0, sticky="w", pady=6)
        self.gender_var = tk.StringVar(value="")
        gender_frame = tk.Frame(form_frame, bg="#ffffff")
        gender_frame.grid(row=row, column=1, sticky="w", pady=6, padx=(12, 0))

        for option in ["Male", "Female", "Other"]:
            rb = tk.Radiobutton(
                gender_frame,
                text=option,
                value=option,
                variable=self.gender_var,
                bg="#ffffff",
                activebackground="#ffffff",
                font=("Segoe UI", 9)
            )
            rb.pack(side=tk.LEFT, padx=(0, 16))
        row += 1

        # Course
        ttk.Label(form_frame, text="Course / Program *").grid(row=row, column=0, sticky="w", pady=6)
        self.course_combo = ttk.Combobox(
            form_frame,
            values=[
                "Computer Science",
                "Information Technology",
                "Data Science & AI",
                "Mechanical Engineering",
                "Civil Engineering",
                "Business Administration",
                "Bio-Technology"
            ],
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.course_combo.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Date of Birth
        ttk.Label(form_frame, text="Date of Birth (DD/MM/YYYY)").grid(row=row, column=0, sticky="w", pady=6)
        self.dob_entry = ttk.Entry(form_frame, font=("Segoe UI", 10))
        self.dob_entry.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Address
        ttk.Label(form_frame, text="Address").grid(row=row, column=0, sticky="nw", pady=6)
        self.address_text = tk.Text(form_frame, height=3, font=("Segoe UI", 10), wrap=tk.WORD, bd=1, relief=tk.SOLID)
        self.address_text.grid(row=row, column=1, sticky="ew", pady=6, padx=(12, 0))
        row += 1

        # Buttons Frame
        btn_frame = tk.Frame(card, bg="#ffffff")
        btn_frame.pack(fill=tk.X, padx=24, pady=(15, 20))

        submit_btn = ttk.Button(
            btn_frame,
            text="Register Student",
            style="Primary.TButton",
            command=self.submit_form
        )
        submit_btn.pack(side=tk.LEFT, padx=(0, 10))

        reset_btn = ttk.Button(
            btn_frame,
            text="Clear Form",
            style="Secondary.TButton",
            command=self.reset_form
        )
        reset_btn.pack(side=tk.LEFT, padx=(0, 10))

        view_btn = ttk.Button(
            btn_frame,
            text="View All Records",
            style="Outline.TButton",
            command=self.view_records
        )
        view_btn.pack(side=tk.RIGHT)

    def validate_inputs(self) -> tuple[bool, str]:
        """Validate required fields and format."""
        roll = self.roll_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        gender = self.gender_var.get().strip()
        course = self.course_combo.get().strip()

        if not roll:
            return False, "Please enter the student's Roll Number / ID."
        if not name:
            return False, "Please enter the student's Full Name."
        if not email:
            return False, "Please enter an Email address."
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "Please enter a valid Email address (e.g., student@example.com)."
        if not phone:
            return False, "Please enter a Phone Number."
        if not re.match(r"^\+?[0-9\s\-]{7,15}$", phone):
            return False, "Please enter a valid Phone Number."
        if not gender:
            return False, "Please select a Gender."
        if not course:
            return False, "Please select a Course."

        return True, ""

    def submit_form(self) -> None:
        """Handle registration and persistence to CSV."""
        is_valid, error_msg = self.validate_inputs()
        if not is_valid:
            messagebox.showerror("Validation Error", error_msg, parent=self.root)
            return

        roll = self.roll_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        gender = self.gender_var.get().strip()
        course = self.course_combo.get().strip()
        dob = self.dob_entry.get().strip()
        address = self.address_text.get("1.0", tk.END).strip()

        # Check for duplicate roll number
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                for row in reader:
                    if row and row[0].strip().lower() == roll.lower():
                        messagebox.showwarning(
                            "Duplicate Entry",
                            f"A student with Roll Number '{roll}' is already registered!",
                            parent=self.root
                        )
                        return

        # Append to CSV
        try:
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([roll, name, email, phone, gender, course, dob, address])

            messagebox.showinfo(
                "Success",
                f"Student '{name}' (Roll No: {roll}) registered successfully!",
                parent=self.root
            )
            self.reset_form()
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to save record:\n{e}", parent=self.root)

    def reset_form(self) -> None:
        """Clear all inputs in the form."""
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.gender_var.set("")
        self.course_combo.set("")
        self.dob_entry.delete(0, tk.END)
        self.address_text.delete("1.0", tk.END)
        self.roll_entry.focus_set()

    def view_records(self) -> None:
        """Open a popup window displaying all registered students in a table."""
        view_win = tk.Toplevel(self.root)
        view_win.title("Registered Students")
        view_win.geometry("850x450")
        view_win.minsize(600, 300)

        # Title
        top_frame = tk.Frame(view_win, bg="#f8fafc", pady=10)
        top_frame.pack(fill=tk.X)
        tk.Label(
            top_frame,
            text="Registered Students Records",
            font=("Segoe UI", 14, "bold"),
            bg="#f8fafc",
            fg="#1e293b"
        ).pack()

        # Table container with scrollbar
        table_frame = tk.Frame(view_win)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=10)

        columns = ("roll", "name", "email", "phone", "gender", "course", "dob", "address")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")

        tree.heading("roll", text="Roll No")
        tree.heading("name", text="Name")
        tree.heading("email", text="Email")
        tree.heading("phone", text="Phone")
        tree.heading("gender", text="Gender")
        tree.heading("course", text="Course")
        tree.heading("dob", text="DOB")
        tree.heading("address", text="Address")

        tree.column("roll", width=80, anchor="center")
        tree.column("name", width=130)
        tree.column("email", width=140)
        tree.column("phone", width=100)
        tree.column("gender", width=70, anchor="center")
        tree.column("course", width=140)
        tree.column("dob", width=90, anchor="center")
        tree.column("address", width=160)

        scrollbar_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=tree.xview)
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        # Load records from CSV
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                count = 0
                for row in reader:
                    if row:
                        tree.insert("", tk.END, values=row)
                        count += 1

                if count == 0:
                    tree.insert("", tk.END, values=("No records found", "", "", "", "", "", "", ""))
        else:
            tree.insert("", tk.END, values=("No records found", "", "", "", "", "", "", ""))


def main():
    root = tk.Tk()
    app = StudentRegistrationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
