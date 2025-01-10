def collectData():
    myDataName = []  # Initialize the list for names
    myDataAge = []   # Initialize the list for ages

    while True:
        name = input("What is your name (enter Exit to quit): ").strip()
        
        if name.lower() == "exit":
            break  # Exit the loop if the user types "exit"
        
        myDataName.append(name)
        
        try:
            age = int(input("How old are you: "))
            myDataAge.append(age)
        except ValueError:
            print("Please enter a valid number for age.")
            # Remove the last name if no valid age is added
            myDataName.pop()
            continue
        
        # Display the last entered name and age
        print(f"The name you've entered is {name} and age is {age}.")
        
        # Create and display the dictionary of names and ages
        myData = dict(zip(myDataName, myDataAge))
        print("Collected Data:", myData)

# Call the function
collectData()
