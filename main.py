from pyscript import document

def candidate_checker(event):
    # List of club members
    club_members = [
        "Joaquin Ortiz", "Allison Burgers", "Ladis Washerum", "Tony Stark", 
        "Steve Rogers", "Clark Kent", "Peter Parker", "Doctor Strange", 
        "Aivind Belen", "Alexander Asis", "Jason Momoa", "Xander Espinosa"
    ]

    # Get user input and format the full name
    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()
    full_name = (f_name + ' ' + l_name).title().strip()

    # Check if the name is in the list
    is_member = full_name in club_members

    # Set messages based on boolean index (True=1, False=0)
    messages = (
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    )

    # Display result and clear inputs
    document.getElementById('result').innerText = messages[is_member]
    document.getElementById('first_name').value = ""
    document.getElementById('last_name').value = ""