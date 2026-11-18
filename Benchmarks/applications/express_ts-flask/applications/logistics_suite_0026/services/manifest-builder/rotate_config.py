# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("rotate_config", __name__)


@bp.route("/rotate_config", methods=["POST"])
def rotate_config():
    citation = request.cookies.get('session_token', '')
    form = FormData(payload=citation)
    parcel = form.payload
    parsed = yaml.safe_load(parcel)
    return jsonify({'parsed': str(parsed)}), 200
