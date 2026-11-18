# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_label", __name__)


@bp.route("/collect_label", methods=["POST"])
def collect_label():
    caption = request.headers.get('Authorization', '')
    parcel = f'{caption!s}'
    yaml.load(parcel, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
