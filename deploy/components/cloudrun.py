# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pulumi_gcp as gcp
from pulumi import Config
from pulumi_gcp.cloudrun import (
    ServiceTemplateMetadataArgs,
    ServiceTemplateSpecContainerEnvArgs,
)

config = Config()


def create_cloud_run_instance(
    cloud_sql_instance: gcp.sql.DatabaseInstance, sql_instance_url: str, image: str
):
    cloud_run = gcp.cloudrun.Service(
        "default-service",
        location=Config("gcp").require("region"),
        template=gcp.cloudrun.ServiceTemplateArgs(
            metadata=ServiceTemplateMetadataArgs(
                annotations={
                    "run.googleapis.com/cloudsql-instances": cloud_sql_instance.connection_name
                }
            ),
            spec=gcp.cloudrun.ServiceTemplateSpecArgs(
                containers=[
                    gcp.cloudrun.ServiceTemplateSpecContainerArgs(
                        image=image,
                        envs=[
                            ServiceTemplateSpecContainerEnvArgs(
                                name="POSTGRES_URI",
                                value=sql_instance_url,
                            )
                        ],
                    )
                ],
            ),
        ),
        traffics=[
            gcp.cloudrun.ServiceTrafficArgs(
                latest_revision=True,
                percent=100,
            )
        ],
    )
    return cloud_run
