# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("verify_bundle", __name__)


@bp.route("/verify_bundle", methods=["POST"])
def verify_bundle():
    notice = request.cookies.get('session_token', '')
    form = FormData(payload=notice)
    persona = form.payload
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
