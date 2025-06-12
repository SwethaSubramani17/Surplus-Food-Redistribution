from donor_form.model.donorform_model import DonorForm
from volunteer_form.model.volunteerform_model import VolunteerForm
from volunteer_form.model import Session

class VolunteerFormController:
    @staticmethod
    def check_donations_available():
        session = Session()
        available_donations = session.query(DonorForm).filter_by(available=True).count()
        session.close()
        return available_donations > 0

    @staticmethod
    def get_volunteer_form(id):
        session = Session()
        volunteer_form = session.query(VolunteerForm).filter_by(id=id).first()
        session.close()
        return volunteer_form

    @staticmethod
    def save_volunteer_decision(id, decision):
        session = Session()
        volunteer_form = session.query(VolunteerForm).filter_by(id=id).first()
        if volunteer_form:
            volunteer_form.decision = decision
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
            # Update the donation status to accepted
            donation.status = 'Accepted'
            session.commit()
        session.close()

    @staticmethod
    def reject_donation(id):
        session = Session()
        donation = session.query(DonorForm).filter_by(id=id).first()
        if donation:
            # Update the donation status to rejected
            donation.status = 'Rejected'
            session.commit()
        session.close()
