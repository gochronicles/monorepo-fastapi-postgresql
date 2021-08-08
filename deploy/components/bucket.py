# Copyright (c) 2021 Go Chronicles
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pulumi_gcp import storage
from components import config


def create_bucket():
    bucket = storage.Bucket(config.require("bucket"))
    return bucket
