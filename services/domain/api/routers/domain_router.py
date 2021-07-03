from fastapi import APIRouter, HTTPException
from api.utils import logger
from api.schemas import Domain, DomainUpdate
from api.exception import DomainException
from api.controllers import DomainController

logging = logger(__name__)

domain_router = APIRouter()


@domain_router.post("/domain")
def createDomain(create_domain_request: Domain):
    """This endpoint creates a new domain record on database. New domain corresponds
    to a new request to Domain API. The primary key for the domain record is "Domain Id"

    Args:
        create_domain_request (Domain): [name: str, total_pages: int, document_count: int, classified: bool]

    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        [Domain]: Returns the detail of the record created.
    """
    logging.debug("Router: /domain")
    logging.debug(
        f"Router createDomain - create_domain_request: {create_domain_request}"
    )

    try:
        return DomainController.create_domain(create_domain_request.dict())
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@domain_router.put("/domain")
def updateDomain(update_domain_request: DomainUpdate):
    """This endpoint updates an existing domain record on database. If there is an
    update required for the database record, this endpoint can be executed.
    Domain id is considered as primary key for the update.

    Args:
        update_domain_request (Domain): [name: str, total_pages: int, document_count: int, classified: bool]
    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        [type]: Returns the detail of the record updated.
    """
    logging.debug("Router: /domain")
    logging.debug(
        f"Router updateDomain - update_domain_request: {update_domain_request}"
    )

    try:
        return DomainController.update_domain(update_domain_request.dict())
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@domain_router.get("/domain")
def getDomain(domain_id: str):
    """Get domain record with domain id.

    Args:
        domain_id (str): domain id for the record. Acts as a primary key.

    Raises:
        HTTPException: returns error if there is no record found with
        the provided domain id.

    Returns:
        Dict: Domain record corresponding to the domain id passed.
    """
    logging.debug("Router: /domain")
    logging.debug(f"Router getDomain - domain_id: {domain_id}")

    try:
        return DomainController.get_domain(domain_id)
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@domain_router.get("/domain/all")
def getAllDomaines():
    """Get all the domaines present in the database.

    Raises:
        HTTPException: raises HTTP Exception if there is any error in underlying CRUD
        operation.

    Returns:
        list: list of all the domaines record.
    """
    logging.debug("Router: /domain/all")
    logging.debug(f"Router getAllDomaines")

    try:
        return DomainController.get_all_domaines()
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@domain_router.delete("/domain")
def deleteDomain(domain_id: str):
    """Delete a domain record with domain id

    Args:
        domain_id (str): unique identifier of the record on database

    Raises:
        HTTPException: Error if there is no such record on database

    Returns:
        null: success response if the record is successfully deleted
    """
    logging.debug("Router: /domain")
    logging.debug(f"Router deleteDomain - domain_id: {domain_id}")

    try:
        return DomainController.delete(domain_id)
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)


@domain_router.delete("/domain/all")
def deleteAllDomaines():
    """Delete all domain record

    Raises:
        HTTPException: raises if there is any error in underlying CRUD
        operation.

    Returns:
        null: success response if all the records are successfully deleted
    """
    logging.debug("Router: /domain/all")
    logging.debug(f"Router deleteAllDomaines")

    try:
        return DomainController.delete_all_domaines()
    except DomainException as response_error:
        raise HTTPException(response_error.status_code, response_error.error_detail)
