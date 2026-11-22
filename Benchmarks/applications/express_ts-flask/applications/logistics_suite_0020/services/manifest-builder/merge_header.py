# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("merge_header", __name__)


@bp.route("/merge_header", methods=["POST"])
def merge_header():
    transcript = request.form.get('field', '')
    pending = list(str(transcript).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    consignment = ','.join(collected)
    Path('/var/app/data/' + str(consignment)).write_text('data')
    return jsonify({"result": "success"})
