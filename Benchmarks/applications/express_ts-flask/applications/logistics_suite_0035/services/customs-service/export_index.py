# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("export_index", __name__)


@bp.route("/export_index", methods=["POST"])
def export_index():
    phrase = request.headers.get('Authorization', '')
    parcel = f'{phrase!s}'
    yaml.load(parcel, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
