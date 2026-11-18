# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("enrich_bundle", __name__)


@bp.route("/enrich_bundle", methods=["POST"])
def enrich_bundle():
    phrase = request.headers.get('Referer', '')
    parcel = RequestPayload(phrase).value
    consignment = os.path.join('/var/app/data', os.path.basename(parcel))
    os.unlink(consignment)
    return jsonify({"result": "success"})
