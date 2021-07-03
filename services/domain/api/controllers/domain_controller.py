from api.crud import CRUDDomain
from api.utils import logger
from api.exception import DomainException

logging = logger(__name__)


class DomainController:
    @staticmethod
    def create_domain(request):
        logging.debug(f"create_domain request parameters: {request}")
        try:
            return CRUDDomain().create(**request)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def update_domain(request: dict):
        logging.debug(f"update_domain request parameters: {request}")
        try:
            return CRUDDomain().update(**request)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_domain(domain_id):
        logging.debug(f"get_domain request parameters: {domain_id}")
        try:
            return CRUDDomain().get(domain_id)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_all_domaines():
        logging.debug(f"get_all_domaines")
        try:
            return CRUDDomain().get_all()
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete(domain_id):
        logging.debug(f"delete request parameters: {domain_id}")
        try:
            return CRUDDomain().delete(domain_id)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete_all_domaines():
        logging.debug(f"delete_all_domaines")
        try:
            return CRUDDomain().delete_all()
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception
