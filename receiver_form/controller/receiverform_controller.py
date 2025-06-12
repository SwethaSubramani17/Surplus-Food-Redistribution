
from donor_form.model.donorform_model import DonorForm
from receiver_form.model import Session

class ReceiverFormController:
    @staticmethod
    def check_donations_available():
        session = Session()
        available_donations = session.query(DonorForm).filter_by(available=True).count()
        session.close()
        return available_donations > 0

    @staticmethod
    def get_receiver_form(id):
        session = Session()
        receiver_form = session.query(ReceiverForm).filter_by(id=id).first()
        session.close()
        return receiver_form

    @staticmethod
    def save_receiver_decision(id, decision):
        session = Session()
        receiver_form = session.query(ReceiverForm).filter_by(id=id).first()
        if receiver_form:
            receiver_form.decision = decision
            session.commit()
        session.close()

    @staticmethod
    def get_donation_details():
        session = Session()
        donations = session.query(DonorForm).all()
        session.close()
        return donations
    
    @staticmethod
    def accept_donation(id):
        session = Session()
        donation = session.query(DonorForm).filter_by(id=id).first()
        if donation:
            # Update the donation availability to True (accepted)
            donation.available = True
            session.commit()
        session.close()

    @staticmethod
    def reject_donation(id):
        session = Session()
        donation = session.query(DonorForm).filter_by(id=id).first()
        if donation:
            # Update the donation availability to False (rejected)
            donation.available = False
            session.commit()
        session.close()
