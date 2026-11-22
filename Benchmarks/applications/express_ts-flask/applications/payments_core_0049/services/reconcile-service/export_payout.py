# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("export_payout", __name__)


@bp.route("/export_payout", methods=["POST"])
def export_payout():
    headline = request.form.get('field', '')
    pending = list(str(headline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    disbursement = ','.join(collected)
    Path('/var/app/data/' + str(disbursement)).write_text('data')
    return jsonify({"result": "success"})
