from pyscript import display, document

def student_club(e):
    first_name = document.getElementById('First_name').value
    last_name = document.getElementById('Last_name').value

    candidate_name = f"{first_name} {last_name}"

    Rainbow_catering = [ 'Ladis Wusherrum','Alison Burgerz','Employs Muswushhands','Optimus Prime', 'Metro Plex', 'Mega Tron']

    member_checker = candidate_name in Rainbow_catering

    display_message = (f"Sorry {candidate_name}, you're not on the list.", f"Congratulations {candidate_name}! You are now part of the Rainbow Catering club." )

    result = document.getElementById('result')
    result.innerHTML = ""
    display(display_message[member_checker], target='result')