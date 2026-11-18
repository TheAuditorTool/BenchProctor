# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("fetch_receipt", __name__)


@bp.route("/fetch_receipt", methods=["POST"])
def fetch_receipt():
    tagline = request.cookies.get('session_token', '')
    form = FormData(payload=tagline)
    rendition = form.payload
    parsed = yaml.safe_load(rendition)
    return jsonify({'parsed': str(parsed)}), 200
