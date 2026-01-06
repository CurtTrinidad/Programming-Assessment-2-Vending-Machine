import datetime # For enabling the date and time function
import pyttsx3 # For text to speech function

engine = pyttsx3.init('sapi5') # Activating the text to speech function with (sapi5)

# Getting the available voices available and setting the first one as default
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(voices[0].id) # Printing the id of the voice selected

# Function to say the given audio text
def say(audio): 
    engine.say(audio)
    engine.runAndWait()
    
# Function to greet the user based on the current time
def date():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().hour - 12, datetime.datetime.now().minute
    
    # Greeting based on the time of the day
    if hour >= 0 and hour <= 12:
        say("Good morning, Welcome to Curt's Vending Machine! What would you like to get!")
    elif hour >= 12 and hour <= 18:
        say("Good afternoon, Welcome to Curt's Vending Machine! What would you like to get!")
    else:
        say("Good evening, Welcome to Curt's Vending Machine! What would you like to get!")
        say("Do you want to get something else?")

# The main block to run the greeting and closing message
if __name__=="__main__":
    date()
    say("Thank you for using Curt's Vending Machine. Come again next time!")

# A variable set global to track the amount of money inserted
amount_due = 0

# Dictionary that contains the items with the details (name, price, category, stock)
items = {
    "D1":{'name':'Water', 'price': 2.00, 'category': 'Drinks', 'stock': 10},
    "D2":{'name':'Coca Cola', 'price': 3.50, 'category': 'Drinks', 'stock': 10},
    "D3":{'name':'Fanta', 'price': 3.50, 'category': 'Drinks', 'stock': 10},
    "D4":{'name':'Sprite', 'price': 3.50, 'category': 'Drinks', 'stock': 10},
    
    "C1":{'name':'Lays', 'price': 2.75, 'category': 'Chips', 'stock': 10},
    "C2":{'name':'Piattos', 'price': 2.75, 'category': 'Chips', 'stock': 10},
    "C3":{'name':'Doritos', 'price': 3.00, 'category': 'Chips', 'stock': 10},
    
    "S1":{'name':'Toblerone', 'price': 6.75, 'category': 'Chocolates', 'stock': 10},
    "S2":{'name':'Mars', 'price': 4.00, 'category': 'Chocolates', 'stock': 10},
    "S3":{'name':'Twix', 'price': 5.00, 'category': 'Chocolates', 'stock': 10}
         } 

# Function to manage the money insertion
def money():
    global amount_due # To access the global amount_due variable
    print("-" * 90) # Printing a separator line
    
    try:
        inserted_money = float(input("Insert money between (1.00 - 50.0): ")) # Asks the user to insert money
    except ValueError:
        print("Invalid Input. Please enter a valid number.") # Handles if the input is invalid
        return # Exits the function
    
    # A checker that checks if the inserted amount is within the allowed range
    if 1.00 <= inserted_money <= 50.0:
        amount_due = amount_due + inserted_money # Adds to the total amount
        print("Your amount inside is $" + str(amount_due)) # Shows the updated amount
    else:
        print("Invalid amount. Please enter a number between (1.00 - 50.0).") # Error message if the inserted amount is less than 1 or more than 50
        
# Function to select a category
def c_category():
    categories = [] # Sets with an empty list for categories
    for item in items.values(): # Looping through all the items
        cat = item["category"] # Takes the category of each item
        if cat not in categories: # Makes it so there is no duplicates
            categories.append(cat) # Adds a unique category to the list
            
    categories.sort() # Sorts the categories alphabetically
    print("\n=== Categories ===") # Prints the categories header
    for i in range(len(categories)): # Looping through all the categories
        print(str(i+1) + "." + categories[i]) # Prints numbered list of categories
    print("X. Exit and Refund") # Shows the option to exit
    
    while True: # Loops through until a valid choice
        choice = input("Select a Category: ").strip().upper() # Gets the user input
        
        if choice == "X": # If the user wants to exit
            return None # To show the user exited
        
        if choice.isdigit(): # Checks if the user input is a number
            num = int(choice) # Will convert the user input into an integer
            if 1 <= num <= len(categories): # Checks if its within the range
                return categories[num-1] # Returns the selected category
            print("Invalid choice. Please select a valid category number or X to exit.") # Prints an error message

# Function that will display all items    
def items_items():

    print("The selection is below") # Displays the header for the menu

    for product_code in items: # Loops through all product codes
        info = items[product_code] # Gets all the item details
        item_name = info["name"] # Takes out the name
        item_price = info["price"] # Takes out the price
        item_stocks = info["stock"] # Takes out the stock

        # Prints the item details in a format string to make it clean 
        print("Code: " + product_code + " | Item: " + item_name.ljust(9) + " | Price: $" + str(item_price) + " | Stocks: " + str(item_stocks))
        
# Function to manage the item selection and buying within a category
def choose_items(category):
    global amount_due # To access the global amount_due variable

    while True: # Main loop for buying
        print("\nAvailable items in "+ category + ":") # Shows the category specific items
        category_items = {} # Dictionary for the items in the selected category
        for code in items: # Loops through all the items
            if items[code]['category'] == category: # Checks if the item matches the category
                category_items[code] = items[code] # Adds to the category_items
                
        if not category_items: # If no items in the category
            print("No items available in this category.") # A message 
            break # Exits the loop
        
        # Displays all the items in the category
        for product_code in category_items:
            item = category_items[product_code]
            item_name = item['name']
            item_price = item['price']
            item_stocks = item['stock']
            print("Code: " + product_code + " | Item: " + item_name.ljust(9) + " | Price: $" + str(item_price) + " | Stocks: " + str(item_stocks))

        choice = input("Enter Item code or type X to EXIT: ").strip().upper() # Gets the user's item choice

        if choice == 'X': # If the user decides to exit 
            print("Your money $" + str(amount_due) + " has been refunded") # Refund message
            amount_due = 0 # Resets the amount
            print("Thank you for using Curt's Vending Machine!") # Thank you message
            break # Exits the loop

        if choice not in category_items: # If the code is invalid
            print("Invalid item code.") # Error message
            continue # Continues the loop

        item = items[choice] # Takes the selected items details

        if item["stock"] <= 0: # Checks the stock if there is any remaining
            print("Sorry, this item is out of stock.") # Out of stock message
            continue # Continues the loop

        if amount_due < item["price"]: # Checks if there is enough money inside 
            due = item["price"] - amount_due # Calculates 
            print("\nInsufficient amount. You need $" + str(due) + " more.") # A message

            print("M - Insert more money") # Option to insert money
            print("O - Cancel and choose another item") # Option to cancel
            print("X - Exit and refund") # Option to exit

            option = input("Choose an option (M/O/X): ").strip().upper() # Takes the option from the user

            if option == 'M': # Insert more money
                money() #  Calls the money function
            elif option == 'O': # Cancel or shows more option
                continue # Continues the loop
            elif option == 'X': # Exits the Vending Machine
                print("\nRefunding remaining amount: $" + str(amount_due)) # Refund message
                amount_due = 0 # Resets the amount inside
                print("Thank you for using Curt's Vending Machine!") # Thank you message
                break # Exits the loop
            else:
                print("Invalid option.") # Error for invalid option 
            continue # Continues the loop

        amount_due = amount_due - item["price"] # Subtracts the price from the amount
        item["stock"] = item["stock"] - 1 # Lessens the stock 

        print("\nDispensing " + item['name'] + " \nSuccessful purchase") # Confirmation of the purchase
        print("Remaining amount: $" + str(amount_due)) # Remaining amount
        
        while True:  # Loop for yes or no question
            y_n = input("Do you want to buy another item? (Y/N): ").strip() # Takes the input
            if y_n == 'No'.lower(): # If no
                print("\nRefunding remaining balance: $ " + str(amount_due)) # Refund message
                amount_due = 0 # Resets the amount
                print("Thank you for using Curt's Vending Machine!") # Thank you message
                return  # Exits the function
            elif y_n == 'Yes'.lower(): # If yes
                break  # Breaks the inside loop
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")  # Error message

# Main program flow
items_items() # Displays the full menu
money() # Handles the money insertion
category = c_category() # The select category
if category is None: # If exited 
    print("Refunding amount: $" + str(amount_due)) # Refund message
    amount_due = 0 # Resets amount
    print("Thank you for using Curt's Vending Machine!") # Thank you message
else:
    choose_items(category) # Continues on to the item selection in category