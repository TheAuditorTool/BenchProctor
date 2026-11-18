# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("enrich_schedule", __name__)


@bp.route("/enrich_schedule", methods=["POST"])
def enrich_schedule():
    subject = request.headers.get('Referer', '')
    ledger = RequestPayload(subject).value
    disbursement = os.path.join('/var/app/data', os.path.basename(ledger))
    os.unlink(disbursement)
    return jsonify({"result": "success"})
