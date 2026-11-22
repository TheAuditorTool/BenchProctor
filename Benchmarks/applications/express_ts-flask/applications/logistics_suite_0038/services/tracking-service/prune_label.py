# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_label", __name__)


@bp.route("/prune_label", methods=["POST"])
def prune_label():
    wording = request.form.get('multipart_field', '')
    parts = str(wording).split(',')
    consignment = ' '.join(parts)
    parsed = json.loads(consignment)
    return jsonify({'parsed': str(parsed)}), 200
