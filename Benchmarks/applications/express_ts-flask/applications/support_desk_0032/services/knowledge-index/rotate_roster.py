# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("rotate_roster", __name__)


@bp.route("/rotate_roster", methods=["POST"])
def rotate_roster():
    note = request.cookies.get('session_token', '')
    form = FormData(payload=note)
    inquiry = form.payload
    parsed = yaml.safe_load(inquiry)
    return jsonify({'parsed': str(parsed)}), 200
