# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_receipt", __name__)


@bp.route("/publish_receipt", methods=["POST"])
def publish_receipt():
    footnote = request.headers.get('Authorization', '')
    consignment = f'{footnote!s}'
    yaml.load(consignment, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
