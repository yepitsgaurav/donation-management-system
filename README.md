# 💰 Simple Donation Management System

This is a basic, terminal-based Python application designed to help manage and track donations and expenses for a small cause or organization.

The application allows users to:
* Add new donors and their donation amounts.
* View a sorted list of all donors and the total collection.
* Search for specific donors.
* Track and manage expenses against the total collection.
* Save all data to a JSON file for persistence.

## ✨ Features

* **Donor Management:** Add, list, and search for donors.
* **Expense Tracking:** Record expenses and automatically update the remaining collection.
* **Data Persistence:** All donor, expense, and total data is saved to `donation_data.json`.
* **Colorized Output:** Uses the `colorama` library for better terminal readability.

## 🛠️ Installation

### Prerequisites

You need **Python 3.x** installed on your system.

### Dependencies

This project uses the `colorama` library for colorful terminal output.

You can install it using `pip`:

```bash
pip install colorama

🚀 How to Run
Clone the repository:

Bash

git clone [https://github.com/yepitsgaurav/donation-management-system.git](https://github.com/yepitsgaurav/donation-management-system.git)
cd donation-management-system
Run the script:

Bash

python main.py
