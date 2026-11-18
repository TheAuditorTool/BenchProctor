# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("enrich_metric", __name__)


@bp.route("/enrich_metric", methods=["POST"])
def enrich_metric():
    caption = request.cookies.get('session_token', '')
    form = FormData(payload=caption)
    cohort = form.payload
    parsed = yaml.safe_load(cohort)
    return jsonify({'parsed': str(parsed)}), 200
