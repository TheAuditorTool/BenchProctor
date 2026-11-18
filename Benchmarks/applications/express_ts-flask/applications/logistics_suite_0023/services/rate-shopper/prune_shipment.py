# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import yaml
from flask import Blueprint, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

bp = Blueprint("prune_shipment", __name__)


@bp.route("/prune_shipment", methods=["POST"])
def prune_shipment():
    caption = request.cookies.get('session_token', '')
    form = FormData(payload=caption)
    parcel = form.payload
    parsed = yaml.safe_load(parcel)
    return jsonify({'parsed': str(parsed)}), 200
