# main.py
from flask import Flask, render_template, request
from controller.volunteer_controller import VolunteerController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('volunteer.html')

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

    # Check if volunteer already exists
    if VolunteerController.check_volunteer_existence(email):
        return render_template('error.html', message=f'Volunteer with email {email} already exists')

    # Register volunteer
    VolunteerController.register_volunteer(name, phone_number, email, password, address)

    return render_template('success.html', message='Registration successful')

if __name__ == '__main__':
    app.run(debug=True)
