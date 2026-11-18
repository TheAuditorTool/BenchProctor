# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("resolve_release", __name__)


@bp.route("/resolve_release", methods=["POST"])
def resolve_release():
    footnote = request.cookies.get('session_token', '')
    form = FormData(payload=footnote)
    wording = form.payload
    parsed = yaml.safe_load(wording)
    return jsonify({'parsed': str(parsed)}), 200
