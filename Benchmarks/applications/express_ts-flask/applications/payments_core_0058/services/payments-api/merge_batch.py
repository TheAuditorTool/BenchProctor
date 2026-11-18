# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("merge_batch", __name__)


@bp.route("/merge_batch", methods=["POST"])
def merge_batch():
    caption = request.form.get('field', '')
    ledger = f'{caption!s}'
    parsed = json.loads(ledger)
    return jsonify({'parsed': str(parsed)}), 200
