# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("collect_ledger", __name__)


@bp.route("/collect_ledger", methods=["POST"])
def collect_ledger():
    citation = request.cookies.get('session_token', '')
    form = FormData(payload=citation)
    backorder = form.payload
    parsed = yaml.safe_load(backorder)
    return jsonify({'parsed': str(parsed)}), 200
