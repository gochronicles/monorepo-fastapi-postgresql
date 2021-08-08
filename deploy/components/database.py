# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pulumi import Output
import pulumi_gcp as gcp
from components import gcp_config, config


def create_database():
    cloud_sql_instance = gcp.sql.DatabaseInstance(
        config.require("db_name"),
        database_version="POSTGRES_12",
        region=gcp_config.require("region"),
        deletion_protection=False,
        settings=gcp.sql.DatabaseInstanceSettingsArgs(
            tier=config.require("db_tier"),
        ),
    )
    _ = gcp.sql.Database(
        "database", instance=cloud_sql_instance.name, name=config.require("db_name")
    )

    _ = gcp.sql.User(
        "users",
        name=config.require("db_name"),
        instance=cloud_sql_instance.name,
        password=config.require_secret("db_password"),
    )

    sql_instance_url = Output.concat(
        "postgres://",
        config.require("db_name"),
        ":",
        config.require_secret("db_password"),
        "@/",
        config.require("db_name"),
        "?host=/cloudsql/",
        cloud_sql_instance.connection_name,
    )
    return cloud_sql_instance, sql_instance_url
