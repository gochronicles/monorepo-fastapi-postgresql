from fastapi import APIRouter, HTTPException
from api.utils import logger
from api.schemas import Patient
from api.exception import PatientException
from api.controllers import PatientController

logging = logger(__name__)

patient_router = APIRouter()


@patient_router.post("/patient")
def createPatient(create_patient_request: Patient):
    """This endpoint creates a new patient record on database. New patient corresponds
    to a new request to Patient API. The primary key for the patient record is "Patient Id"

    Args:
        create_patient_request (Patient): [name: str, total_pages: int, document_count: int,
       classified: bool]

    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        [Patient]: Returns the detail of the record created.
    """
    logging.debug("Router: /patient")
    logging.debug(
        f"Router createPatient - create_patient_request: {create_patient_request}"
    )

    try:
        return PatientController.create_patient(create_patient_request.dict())
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@patient_router.put("/patient")
def updatePatient(update_patient_request: Patient):
    """This endpoint updates an existing patient record on database. If there is an
    update required for the database record, this endpoint can be executed.
    Patient id is considered as primary key for the update.

    Args:
        update_patient_request (Patient): [name: str, total_pages: int, document_count: int,
       classified: bool]

    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        [type]: Returns the detail of the record updated.
    """
    logging.debug("Router: /patient")
    logging.debug(
        f"Router updatePatient - update_patient_request: {update_patient_request}"
    )

    try:
        return PatientController.update_patient(update_patient_request.dict())
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@patient_router.get("/patient")
def getPatient(patient_id: str):
    """Get patient record with patient id.

    Args:
        patient_id (str): patient id for the record. Acts as a primary key.

    Raises:
        HTTPException: returns error if there is no record found with
        the provided patient id.

    Returns:
        Dict: Patient record corresponding to the patient id passed.
    """
    logging.debug("Router: /patient")
    logging.debug(f"Router getPatient - patient_id: {patient_id}")

    try:
        return PatientController.get_patient(patient_id)
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@patient_router.get("/patient/all")
def getAllPatientes():
    """Get all the patientes present in the database.

    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        list: list of all the patientes record.
    """
    logging.debug("Router: /patient/all")
    logging.debug(f"Router getAllPatientes")

    try:
        return PatientController.get_all_patientes()
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@patient_router.delete("/patient")
def deletePatient(patient_id: str):
    """Delete a patient record with patient id

    Args:
        patient_id (str): unique identifier of the record on database

    Raises:
        HTTPException: Error if there is no such record on database

    Returns:
        null: success response if the record is successfully deleted
    """
    logging.debug("Router: /patient")
    logging.debug(f"Router deletePatient - patient_id: {patient_id}")

    try:
        return PatientController.delete(patient_id)
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@patient_router.delete("/patient/all")
def deleteAllPatientes():
    """Delete all patient record

    Raises:
        HTTPException: raises if there is any error in underlying CRUD
        operation.

    Returns:
        null: success response if all the records are successfully deleted
    """
    logging.debug("Router: /patient/all")
    logging.debug(f"Router deleteAllPatientes")

    try:
        return PatientController.delete_all_patientes()
    except PatientException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)
