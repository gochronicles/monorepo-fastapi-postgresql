import logging
from pathlib import os


def get_file_handler(
    log_name: str, mode: int, formatter: logging.Formatter, save_path: str = "./logs"
):
    os.makedirs(save_path, exist_ok=True)
    # file logs
    file_handler = logging.FileHandler(
        filename=os.path.join(save_path, log_name), mode="a"
    )
    file_handler.setLevel(mode)
    file_handler.setFormatter(formatter)
    return file_handler


def config_logger(logger: logging.Logger, debug_mode: bool = True):
    formatter = logging.Formatter(
        "[pid=%(process)s] - [%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]"
    )
    console_handler = logging.StreamHandler()  # console handler
    console_handler.setLevel(logging.DEBUG)
    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    # file logs
    debug_logger = get_file_handler(
        log_name="debug.log", mode=logging.DEBUG, formatter=formatter
    )
    info_logger = get_file_handler(
        log_name="info.log", mode=logging.INFO, formatter=formatter
    )
    error_logger = get_file_handler(
        log_name="error.log", mode=logging.ERROR, formatter=formatter
    )
    logger.addHandler(debug_logger)
    logger.addHandler(info_logger)
    logger.addHandler(error_logger)
    # logging level set to DEBUG
    logger.setLevel(logging.DEBUG)
    return logger


def logger(__name__):
    logging_obj = config_logger(logging.getLogger(__name__))
    return logging_obj