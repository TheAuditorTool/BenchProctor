# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_label", __name__)


@bp.route("/collect_label", methods=["POST"])
def collect_label():
    subject = request.headers.get('Origin', '')
    pending = list(str(subject).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    parcel = ','.join(collected)
    parsed = yaml.safe_load(parcel)
    return jsonify({'parsed': str(parsed)}), 200
