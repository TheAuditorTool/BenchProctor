# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("render_waybill", __name__)


@bp.route("/render_waybill", methods=["POST"])
def render_waybill():
    footnote = request.headers.get('Origin', '')
    pending = list(str(footnote).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    parcel = ','.join(collected)
    parsed = yaml.safe_load(parcel)
    return jsonify({'parsed': str(parsed)}), 200
