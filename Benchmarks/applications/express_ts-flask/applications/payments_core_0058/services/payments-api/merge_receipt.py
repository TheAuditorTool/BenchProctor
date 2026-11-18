# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("merge_receipt", __name__)


@bp.route("/merge_receipt", methods=["POST"])
def merge_receipt():
    caption = request.headers.get('Referer', '')
    ledger = RequestPayload(caption).value
    remittance = os.path.join('/var/app/data', os.path.basename(ledger))
    os.unlink(remittance)
    return jsonify({"result": "success"})
