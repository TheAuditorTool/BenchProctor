# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("audit_batch", __name__)


@bp.route("/audit_batch", methods=["POST"])
def audit_batch():
    wording = request.form.get('multipart_field', '')
    try:
        addendum = json.loads(wording).get('value', wording)
    except (json.JSONDecodeError, AttributeError):
        addendum = wording
    os.unlink('/var/app/data/' + str(addendum))
    return jsonify({"result": "success"})
