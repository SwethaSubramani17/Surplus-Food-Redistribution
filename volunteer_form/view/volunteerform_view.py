from flask import Flask, render_template
from controller.volunteerform_controller import VolunteerFormController

app = Flask(__name__, template_folder='view/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteerform/<int:id>')
def show_volunteer_form(id):
    volunteer_form = VolunteerFormController.get_volunteer_form(id)
    return render_template('volunteerform.html', volunteer_form=volunteer_form)

if __name__ == '__main__':
    app.run(debug=True)