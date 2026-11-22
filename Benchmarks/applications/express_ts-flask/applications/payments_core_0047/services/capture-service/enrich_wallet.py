# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("enrich_wallet", __name__)


@bp.route("/enrich_wallet", methods=["POST"])
def enrich_wallet():
    footnote = request.headers.get('X-Forwarded-For', '')
    remittance = footnote if footnote else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    disbursement = remittance
    Path('/var/app/data/' + str(disbursement)).write_text('data')
    return jsonify({"result": "success"})
