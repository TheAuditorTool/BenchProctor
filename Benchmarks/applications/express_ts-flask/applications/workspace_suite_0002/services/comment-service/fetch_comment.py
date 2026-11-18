# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("fetch_comment", __name__)


@bp.route("/fetch_comment", methods=["POST"])
def fetch_comment():
    transcript = request.cookies.get('session_token', '')
    form = FormData(payload=transcript)
    heading = form.payload
    parsed = yaml.safe_load(heading)
    return jsonify({'parsed': str(parsed)}), 200
