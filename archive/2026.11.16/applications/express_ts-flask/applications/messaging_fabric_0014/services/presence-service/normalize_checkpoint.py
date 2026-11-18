# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_checkpoint", __name__)


@bp.route("/normalize_checkpoint", methods=["POST"])
def normalize_checkpoint():
    summary = request.headers.get('Origin', '')
    pending = list(str(summary).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    bulletin = ','.join(collected)
    parsed = yaml.safe_load(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
