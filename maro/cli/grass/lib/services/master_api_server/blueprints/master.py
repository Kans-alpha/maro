# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


from flask import Blueprint, request

from ..objects import redis_controller, service_config

# Flask related.

blueprint = Blueprint(name="master", import_name=__name__, url_prefix="/master")


# Api functions.

@blueprint.route("", methods=["GET"])
def get_master():
    """Get master.

    Returns:
        None.
    """

    master_details = redis_controller.get_master_details(cluster_name=service_config["cluster_name"])
    return master_details


@blueprint.route("", methods=["POST"])
def create_master():
    """Create master.

    Returns:
        None.
    """

    master_details = request.json
    redis_controller.set_master_details(
        cluster_name=service_config["cluster_name"],
        master_details=master_details
    )
    return {}


@blueprint.route("", methods=["DELETE"])
def delete_master():
    """Delete master.

    Returns:
        None.
    """

    redis_controller.delete_master_details(cluster_name=service_config["cluster_name"])
    return {}