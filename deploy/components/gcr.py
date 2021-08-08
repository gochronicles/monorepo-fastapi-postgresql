# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pulumi import Output
from pulumi_docker import Image, DockerBuild
from components import gcp_config, config


def create_gcr_image(image_name: str):
    project = gcp_config.require("project")
    image = Image(
        image_name,
        Output.concat(f"gcr.io/{project}/{image_name}:latest"),
        build=DockerBuild(
            dockerfile=f"../services/{image_name}/Dockerfile",
            env={"mode": config.require("mode")},
        ),
    )
    return image
