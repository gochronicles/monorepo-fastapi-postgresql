# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pulumi_gcp as gcp
from pulumi import ProviderResource
from pulumi_gcp.cloudrun import (
    ServiceTemplateMetadataArgs,
    ServiceTemplateSpecContainerEnvArgs,
)
from components import config, gcp_config


def create_cloud_run_instance(
    cloud_sql_instance: gcp.sql.DatabaseInstance, sql_instance_url: str, image: str
):

    cloud_run = gcp.cloudrun.Service(
        "default-service",
        location=gcp_config.require("region"),
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
                            ),
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
    _ = gcp.cloudrun.IamMember(
        "cr_everyone",
        service=cloud_run.name,
        location=gcp_config.require("region"),
        role="roles/run.invoker",
        member="allUsers",
    )  # enable public access to URL
    return cloud_run
