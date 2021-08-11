# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from uuid import uuid4
from pulumi_gcp.container import Registry, get_registry_repository
from pulumi_docker import Image, DockerBuild
from components import config


def create_gcr_image(name: str):
    hash = str(uuid4()).split("-")[-1]
    registry_name = f"registry-{hash}"
    registry = Registry(registry_name)
    registry_url = registry.id.apply(lambda _: get_registry_repository().repository_url)
    image_name = registry_url.apply(lambda url: f"{url}/{name}")
    image = Image(
        name=name,
        image_name=image_name,
        build=DockerBuild(
            context=f"../services/{name}",
            env={"mode": config.require("mode")},
        ),
        registry=None,
    )
    return image
