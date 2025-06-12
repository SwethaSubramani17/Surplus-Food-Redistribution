from flask import Flask, render_template, request
from controller.donorform_controller import DonorFormController

app = Flask(__name__, template_folder='view/templates')

@app.route('/')
def index():
    return render_template('donorform.html')

@app.route('/submit', methods=['POST'])
def submit_donor_form():
    try:
        # Get form data
        donor_name = request.form.get('donor_name')
        food_name = request.form.get('food_name')
        food_type = request.form.get('food_type')
        quantity = int(request.form.get('quantity'))
        preparation_time = request.form.get('preparation_time')
        
        # Save donor form
        DonorFormController.save_donor_form(donor_name, food_name, food_type, quantity, preparation_time)
        
        # Render success template
        return render_template('success.html', message='Thank you for your donation!')
    
    except Exception as e:
        # Handle exceptions
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

@app.route('/success')
def success():
    return render_template('success.html', message='Thank you for your donation!')

if __name__ == '__main__':
    app.run(debug=True)

