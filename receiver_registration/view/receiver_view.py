class ReceiverView:
    @staticmethod
    def get_receiver_details():
        name = input("Enter your name: ")
        phone_number = input("Enter your phone_number: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        address = input("Enter your address: ")
        return name, phone_number, email, password, confirm_password, address

    @staticmethod
    def display_receiver_existence_message(email, exists):
        if exists:
            print(f"Receiver with email {email} already exists.")
        else:
            print(f"Receiver with email {email} does not exist.")

    @staticmethod
    def display_registration_success_message(name):
        print(f"Registration successful! Thank you, {name}, for registering as a receiver.")

    @staticmethod
    def display_registration_error_message():
        print("There was an error processing your registration. Please try again.")

    @staticmethod
    def display_password_mismatch_message():
        print("Password and confirm password do not match. Please try again.")
