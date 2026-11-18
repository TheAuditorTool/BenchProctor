# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("archive_checkpoint", __name__)


@bp.route("/archive_checkpoint", methods=["POST"])
def archive_checkpoint():
    snippet = request.cookies.get('session_token', '')
    form = FormData(payload=snippet)
    persona = form.payload
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
