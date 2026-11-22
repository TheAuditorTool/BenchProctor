# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("summarize_receipt", __name__)


@bp.route("/summarize_receipt", methods=["POST"])
def summarize_receipt():
    remark = request.form.get('field', '')
    pending = list(str(remark).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    inquiry = ','.join(collected)
    Path('/var/app/data/' + str(inquiry)).write_text('data')
    return jsonify({"result": "success"})
