from datetime import datetime
from uuid import uuid4
from api.crud.crud_base import CRUDBase
from api import session
from api.utils import logger
from api.exception import (
    PatientException,
    GENERIC_database_error,
    DOMAIN_patient_not_found,
)
from api.orm_models import Patient


logging = logger(__name__)


class CRUDPatient(CRUDBase):
    def __init__(self):
        super().__init__()

    def create(self, **kwargs):
        logging.debug(f"CRUDPatient create - {kwargs}")

        try:
            patient = Patient(**kwargs)
            current_time = datetime.now()
            patient.patient_id = str(uuid4())
            patient.created_timestamp = current_time
            patient.updated_timestamp = current_time

            with session() as transaction_session:
                transaction_session.add(patient)
                transaction_session.commit()
                transaction_session.refresh(patient)
            return patient
        except Exception as error_info:
            raise PatientException(
                GENERIC_database_error, exception_object=error_info, error_input=kwargs
            )

    def update(self, **kwargs):
        logging.debug(f"CRUDPatient update - {kwargs}")
        try:
            with session() as transaction_session:
                obj: Patient = transaction_session.query(Patient).get(
                    kwargs.get("patient_id")
                )
                if obj is None:
                    raise PatientException(DOMAIN_patient_not_found, error_input=kwargs)
                obj.name = kwargs.get("name")
                obj.total_pages = kwargs.get("total_pages")
                obj.document_count = kwargs.get("document_count")
                obj.classified = kwargs.get("classified")
                obj.updated_timestamp = datetime.now()
                transaction_session.commit()
                transaction_session.refresh(obj)
            return obj
        except PatientException as sbox_exception:
            raise sbox_exception
        except Exception as error_info:
            raise PatientException(
                GENERIC_database_error, exception_object=error_info, error_input=kwargs
            )

    def get_all(self):
        logging.debug("CRUDPatient get_all")

        try:
            with session() as transaction_session:
                orm_results = transaction_session.query(Patient).all()
                return [row.__dict__ for row in orm_results]
        except Exception as error_info:
            raise PatientException(GENERIC_database_error, exception_object=error_info)

    def get(self, patient_id):
        logging.debug(f"CRUDPatient get - patient_id: {patient_id}")

        try:
            with session() as transaction_session:
                orm_result = transaction_session.query(Patient).get(patient_id)
                if orm_result is None:
                    return []
                return orm_result.__dict__
        except Exception as error_info:
            raise PatientException(
                GENERIC_database_error,
                exception_object=error_info,
                error_input={"patient_id": patient_id},
            )

    def delete(self, patient_id):
        logging.debug(f"CRUDPatient delete - patient_id: {patient_id}")
        try:
            with session() as transaction_session:
                transaction_session.query(Patient).filter(
                    Patient.patient_id == patient_id
                ).delete()
                transaction_session.commit()
        except Exception as error_info:
            raise PatientException(
                GENERIC_database_error,
                exception_object=error_info,
                error_input={"patient_id": patient_id},
            )

    def delete_all(self):
        logging.debug(f"CRUDPatient delete_all")
        try:
            with session() as transaction_session:
                transaction_session.query(Patient).delete()
                transaction_session.commit()
        except Exception as error_info:
            raise PatientException(
                GENERIC_database_error,
                exception_object=error_info,
            )
