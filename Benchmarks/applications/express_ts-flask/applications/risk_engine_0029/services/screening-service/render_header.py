# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("render_header", __name__)


@bp.route("/render_header", methods=["POST"])
def render_header():
    subject = request.cookies.get('session_token', '')
    form = FormData(payload=subject)
    grievance = form.payload
    parsed = yaml.safe_load(grievance)
    return jsonify({'parsed': str(parsed)}), 200
