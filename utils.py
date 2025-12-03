def get_choice(prompt, valid_choices=None):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if valid_choices is not None and user_input not in valid_choices:
            print(f"Veuillez entrer une des valeurs suivantes : {valid_choices}")
            continue
        return user_input