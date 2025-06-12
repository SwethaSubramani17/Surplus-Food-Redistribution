from flask import Flask, render_template
from controller.receiverform_controller import ReceiverFormController

app = Flask(__name__, template_folder='view/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receiverform/<int:id>')
def show_receiver_form(id):
    receiver_form = ReceiverFormController.get_receiver_form(id)
    return render_template('receiverform.html', receiver_form=receiver_form)

if __name__ == '__main__':
    app.run(debug=True)
