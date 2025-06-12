from model.donorform_model import DonorForm
from model.database import Session  # Import Session from your database module

class DonorFormController:
    @staticmethod
    def save_donor_form(donor_name, food_name, food_type, quantity, preparation_time):
        session = Session()  # Instantiate Session outside the try block
        try:
            donor_form = DonorForm(donor_name=donor_name, food_name=food_name, food_type=food_type, quantity=quantity, preparation_time=preparation_time)
            session.add(donor_form)
            session.commit()
            return True
        except Exception as e:
            print("Failed to save donor form:", str(e))
            return False
        finally:
            session.close()  # Ensure session is closed even if an exception occurs
