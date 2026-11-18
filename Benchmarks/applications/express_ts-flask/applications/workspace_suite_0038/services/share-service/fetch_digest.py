# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("fetch_digest", __name__)


@bp.route("/fetch_digest", methods=["POST"])
def fetch_digest():
    preface = request.cookies.get('session_token', '')
    form = FormData(payload=preface)
    remark = form.payload
    parsed = yaml.safe_load(remark)
    return jsonify({'parsed': str(parsed)}), 200
