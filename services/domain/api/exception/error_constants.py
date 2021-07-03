GENERIC_no_records_found = {
    "error_code": "1000",
    "error_message": "No records found",
    "status_code": 404,
}

GENERIC_bad_request = {
    "error_code": "1001",
    "error_mesasage": "Request body was malformed",
    "status_code": 400,
}

GENERIC_unauthorized = {
    "error_code": "1002",
    "error_message": "Unauthorized",
    "status_code": 401,
}

GENERIC_db_connection = {
    "error_code": "1003",
    "error_message": "Could not connect to DB",
    "status_code": 500,
}

GENERIC_db_session = {
    "error_code": "1004",
    "error_message": "DB session failed to connect",
    "status_code": 500,
}

GENERIC_internal_error = {
    "error_code": "1005",
    "error_message": "Internal server error",
    "status_code": 500,
}

GENERIC_unknown_error = {
    "error_code": "1006",
    "error_message": "Error object was malformed",
    "status_code": 500,
}
GENERIC_forbidden = {
    "error_code": "1007",
    "error_message": "This action is forbidden",
    "status_code": 403,
}
GENERIC_miscellaneous = {
    "error_code": "1008",
    "error_message": "Something went wrong.",
    "status_code": 500,
}
GENERIC_database_error = {
    "error_code": "1009",
    "error_message": "Database internal error",
    "status_code": 500,
}

DOMAIN_domain_not_found = {
    "error_code": "6001",
    "error_message": "Domain not found",
    "status_code": 404,
}


STATUS_domain_file_not_found = {
    "error_code": "10000",
    "error_message": "Did not find the domain or file to update status",
    "status_code": 404,
}