from model.receiver_model import Session, Receiver

class ReceiverController:
    @staticmethod
    def register_receiver(name, phone_number, email, password, address):
        session = Session()
        new_receiver = Receiver(name=name, phone_number=phone_number, email=email, password=password, address=address)
        session.add(new_receiver)
        session.commit()
        session.close()

    @staticmethod
    def check_receiver_existence(email):
        session = Session()
        receiver = session.query(Receiver).filter_by(email=email).first()
        session.close()
        return receiver is not None
