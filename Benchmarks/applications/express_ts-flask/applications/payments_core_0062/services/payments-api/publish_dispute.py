# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("publish_dispute", __name__)


@bp.route("/publish_dispute", methods=["POST"])
def publish_dispute():
    headline = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    disbursement = normalize(headline)
    with open('/var/app/data/' + str(disbursement), 'r') as fh:
        content = fh.read()
    return content
