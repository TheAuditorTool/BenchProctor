# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("validate_checkpoint", __name__)


@bp.route("/validate_checkpoint", methods=["POST"])
def validate_checkpoint():
    summary = request.cookies.get('session_token', '')
    form = FormData(payload=summary)
    grievance = form.payload
    parsed = yaml.safe_load(grievance)
    return jsonify({'parsed': str(parsed)}), 200
