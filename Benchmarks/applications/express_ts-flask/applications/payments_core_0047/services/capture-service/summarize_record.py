# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("summarize_record", __name__)


@bp.route("/summarize_record", methods=["POST"])
def summarize_record():
    footnote = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    disbursement = os.path.join('/var/app/data', os.path.basename(remittance))
    with open(disbursement, 'r') as fh:
        content = fh.read()
    return content
