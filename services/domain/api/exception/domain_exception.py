from api.exception import GENERIC_unknown_error
from api.utils import logger
import traceback
import json

logging = logger(__name__)


class DomainException(Exception):
    def __init__(
        self,
        error_object: dict = GENERIC_unknown_error,
        exception_object: Exception = None,
        additional_error_info: tuple = None,
        error_input: dict = None,
    ):

        # Properties
        self.error_message = error_object.get("error_message")
        self.error_code = error_object.get("error_code")
        self.status_code = error_object.get("status_code")
        self.additional_error_info = additional_error_info
        self.error_input = json.dumps(error_input) if error_input else None

        if exception_object:
            self.exception_traceback = " ".join(
                traceback.format_tb(tb=exception_object.__traceback__)
            )
            if not self.additional_error_info:
                # If there is no additional info, use error args
                self.additional_error_info = exception_object.args
        else:
            self.exception_traceback = None

        self.error_detail = {
            "message": self.error_message,
            "error_code": self.error_code,
            "additional_info": self.additional_error_info,
        }
        logging.error(
            f"Exception raised with: Status Code - {self.status_code} Error Detail - {self.error_detail}"
        )

        self.error_log_object = {
            "error_message": self.error_message,
            "error_code": self.error_code,
            "additional_error_info": self.additional_error_info,
            "exception_traceback": self.exception_traceback,
            "error_input": self.error_input,
            "domain_id": error_input.get("domain_id") if error_input else None,
        }
