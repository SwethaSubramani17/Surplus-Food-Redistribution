@app.route('/receiverform/<int:id>')
def show_receiver_form(id):
    receiver_form = ReceiverFormController.get_receiver_form(id)
    if receiver_form:
        image_url = f'receiverform/{id}/image'
        return render_template('receiverform.html', receiver_form=receiver_form, image_url=image_url)
    else:
        flash('Food donation not found', 'danger')
        return redirect(url_for('index'))
