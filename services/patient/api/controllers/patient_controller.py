from api.crud import CRUDPatient
from api.utils import logger
from api.exception import PatientException

logging = logger(__name__)


class PatientController:
    @staticmethod
    def create_patient(request):
        logging.debug(f"create_patient request parameters: {request}")
        try:
            return CRUDPatient().create(**request)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def update_patient(request: dict):
        logging.debug(f"update_patient request parameters: {request}")
        try:
            return CRUDPatient().update(**request)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_patient(patient_id):
        logging.debug(f"get_patient request parameters: {patient_id}")
        try:
            return CRUDPatient().get(patient_id)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_all_patientes():
        logging.debug(f"get_all_patientes")
        try:
            return CRUDPatient().get_all()
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete(patient_id):
        logging.debug(f"delete request parameters: {patient_id}")
        try:
            return CRUDPatient().delete(patient_id)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete_all_patientes():
        logging.debug(f"delete_all_patientes")
        try:
            return CRUDPatient().delete_all()
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception
