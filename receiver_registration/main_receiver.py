from flask import Flask, render_template, request
from controller.receiver_controller import ReceiverController

app = Flask(__name__, template_folder='view/templates')

@app.route('/')
def index():
    return render_template('receiver.html')

@app.route('/register', methods=['POST'])
def register():
    # Extract form data
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    address = request.form.get('address')

   # Check if passwords match
    if password != confirm_password:
        return render_template('error.html', message='Passwords do not match')

    # Check if receiver already exists
    if ReceiverController.check_receiver_existence(email):
        return render_template('error.html', message=f'Receiver with email {email} already exists')

    # Register receiver
    ReceiverController.register_receiver(name, phone_number, email, password, address)

    return render_template('success.html', message='Registration successful')

if __name__ == '__main__':
    app.run(debug=True)
