'''
This is a simple Flask application that provides a basic CRUD for managing transactions.
It allows users to add, edit, delete, and search for transactions.
The application uses Flask's routing system to define different endpoints for each operation.
This also includes a simple HTML template rendering system to display the transactions and forms.
The application is structured with the following routes:
1. `/` - Displays all transactions.
2. `/add` - Allows users to add a new transaction.
3. `/edit/<transaction_id>` - Allows users to edit an existing transaction.
4. `/delete/<transaction_id>` - Allows users to delete a transaction.
5. `/search` - Allows users to search for transactions based on a specified amount range.
6. `/balance` - Displays the total balance of all transactions.
This application is a basic example of how to use Flask for web development.
'''
# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route('/')
def get_transactions():
    '''
    This function handles the root URL and retrieves all transactions.
    It renders the transactions.html template and passes the transactions data to it.
    '''
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route('/add', methods = ['GET', 'POST'])
def add_transaction():
    '''
    This function handles the '/add' URL and allows users to add a new transaction.
    It supports both GET and POST methods.
    If the request method is POST, it processes the form data and adds a new transaction.
    If the request method is GET, it renders the form.html template.
    '''
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,            # Generate a new ID
            'date': request.form['date'],           # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")

# Update operation
@app.route('/edit/<int:transaction_id>', methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    '''
    This function handles the '/edit/<transaction_id>' URL
    It supports both GET and POST methods.
    If the request method is POST, it processes the form data and updates the transaction.
    If the request method is GET, it retrieves the transaction and renders the edit.html template.
    '''
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']           # Get the 'date' field value from the form
        amount = float(request.form['amount'])# Get the 'amount' field value
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break                            # Exit the loop once the transaction is found
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))
    # If the request method is GET, find the transaction with the ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    '''
    This function handles the '/delete/<transaction_id>' URL.
    It finds the transaction with the specified ID and removes it from the transactions list.
    After deletion, it redirects to the transactions list page.
    '''
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions.copy():
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

@app.route('/search', methods = ['GET', 'POST'])
def search_transactions():
    '''
    This function handles the '/search' URL.
    It supports both GET and POST methods.
    If the method is POST, it processes the form data and filters transactions based on the range.
    If the request method is GET, it renders the search.html template to display the search form.
    '''
    if request.method == 'POST':
        # Get the min and max amount from the form
        min_value = float(request.form['min_amount'])
        max_value = float(request.form['max_amount'])
        # Filter transactions based on the amount range
        filtered_transactions = []  # Initialize an empty list to store filtered transactions
        for amount in range(int(min_value), int(max_value) + 1):
            # Iterate through the transactions and check if the amount is within the range
            for transaction in transactions:
                if transaction['amount'] == amount:
                    filtered_transactions.append(transaction)
        # Render the search results template with the filtered transactions
        return render_template("transactions.html", transactions=filtered_transactions)
    return render_template("search.html")

@app.route('/balance')
def total_balance():
    '''
    This function handles the '/balance' URL and calculates the total balance of all transactions.
    It retrieves all transactions and sums their amounts to calculate the total balance,
    then renders the transactions.html and passes the transactions and total balance to it.
    '''
    # Calculate the total balance by summing the 'amount' field of all transactions
    total = sum(transaction['amount'] for transaction in transactions)
    # Render the transactions template, pass the transactions and the total balance value
    return render_template("transactions.html", transactions=transactions, total_balance=total)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=False)
