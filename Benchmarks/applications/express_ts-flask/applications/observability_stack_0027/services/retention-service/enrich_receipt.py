# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("enrich_receipt", __name__)


@bp.route("/enrich_receipt", methods=["POST"])
def enrich_receipt():
    remark = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(remark)
    with open('/var/app/data/' + str(gauge), 'r') as fh:
        content = fh.read()
    return content
