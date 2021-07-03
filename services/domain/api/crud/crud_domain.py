from datetime import datetime
from uuid import uuid4
from api.crud.crud_base import CRUDBase
from api import session
from api.utils import logger
from api.exception import (
    DomainException,
    GENERIC_database_error,
    DOMAIN_domain_not_found,
)
from api.orm_models import Domain


logging = logger(__name__)


class CRUDDomain(CRUDBase):
    def __init__(self):
        super().__init__()

    def create(self, **kwargs):
        logging.debug(f"CRUDDomain create - {kwargs}")

        try:
            domain = Domain(**kwargs)
            current_time = datetime.now()
            domain.domain_id = str(uuid4())
            domain.created_timestamp = current_time
            domain.updated_timestamp = current_time

            with session() as transaction_session:
                transaction_session.add(domain)
                transaction_session.commit()
                transaction_session.refresh(domain)
            return domain
        except Exception as error_info:
            raise DomainException(
                GENERIC_database_error, exception_object=error_info, error_input=kwargs
            )

    def update(self, **kwargs):
        logging.debug(f"CRUDDomain update - {kwargs}")
        try:
            with session() as transaction_session:
                obj: Domain = transaction_session.query(Domain).get(
                    kwargs.get("domain_id")
                )
                if obj is None:
                    raise DomainException(DOMAIN_domain_not_found, error_input=kwargs)
                obj.name = kwargs.get("total_pages")
                obj.total_pages = kwargs.get("total_pages")
                obj.document_count = kwargs.get("document_count")
                obj.classified = kwargs.get("classified")
                obj.updated_timestamp = datetime.now()
                transaction_session.commit()
                transaction_session.refresh(obj)
            return obj
        except DomainException as sbox_exception:
            raise sbox_exception
        except Exception as error_info:
            raise DomainException(
                GENERIC_database_error, exception_object=error_info, error_input=kwargs
            )

    def get_all(self):
        logging.debug("CRUDDomain get_all")

        try:
            with session() as transaction_session:
                orm_results = transaction_session.query(Domain).all()
                return [row.__dict__ for row in orm_results]
        except Exception as error_info:
            raise DomainException(GENERIC_database_error, exception_object=error_info)

    def get(self, domain_id):
        logging.debug(f"CRUDDomain get - domain_id: {domain_id}")

        try:
            with session() as transaction_session:
                orm_result = transaction_session.query(Domain).get(domain_id)
                if orm_result is None:
                    return []
                return orm_result.__dict__
        except Exception as error_info:
            raise DomainException(
                GENERIC_database_error,
                exception_object=error_info,
                error_input={"domain_id": domain_id},
            )

    def delete(self, domain_id):
        logging.debug(f"CRUDDomain delete - domain_id: {domain_id}")
        try:
            with session() as transaction_session:
                transaction_session.query(Domain).filter(
                    Domain.domain_id == domain_id
                ).delete()
                transaction_session.commit()
        except Exception as error_info:
            raise DomainException(
                GENERIC_database_error,
                exception_object=error_info,
                error_input={"domain_id": domain_id},
            )

    def delete_all(self):
        logging.debug(f"CRUDDomain delete_all")
        try:
            with session() as transaction_session:
                transaction_session.query(Domain).delete()
                transaction_session.commit()
        except Exception as error_info:
            raise DomainException(
                GENERIC_database_error,
                exception_object=error_info,
            )
