@app.route('/volunteerform/<int:id>')
def show_volunteer_form(id):
    volunteer_form = VolunteerFormController.get_volunteer_form(id)
    if volunteer_form:
        image_url = f'/receiverform/{id}/image'
        return render_template('volunteerform.html', volunteer_form=volunteer_form, image_url=image_url)
    else:
        flash('Food donation not found', 'danger')
        return redirect(url_for('index'))