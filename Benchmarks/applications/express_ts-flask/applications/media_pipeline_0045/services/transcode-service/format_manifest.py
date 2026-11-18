# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("format_manifest", __name__)


@bp.route("/format_manifest", methods=["POST"])
def format_manifest():
    notice = request.cookies.get('session_token', '')
    form = FormData(payload=notice)
    rendition = form.payload
    parsed = yaml.safe_load(rendition)
    return jsonify({'parsed': str(parsed)}), 200
