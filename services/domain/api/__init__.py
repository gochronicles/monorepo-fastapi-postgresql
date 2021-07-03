from pathlib import os
from api.utils import load_config

# Load Config
config_path = os.getenv("DOMAIN_CONFIG", "config.yml")
config = load_config(config_path)

# Database Manager
from api.database.database_manager import DatabaseManager

database_manager = DatabaseManager.sharedInstance()
Base = database_manager.Base

# Context
from api.database.context_manager import session

# Create Tables
from api.orm_models import Domain

Base.metadata.create_all(bind=database_manager.engine)

from api.api import app