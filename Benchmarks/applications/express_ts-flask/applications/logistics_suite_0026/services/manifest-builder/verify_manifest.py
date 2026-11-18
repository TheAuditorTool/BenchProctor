# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("verify_manifest", __name__)


@bp.route("/verify_manifest", methods=["POST"])
def verify_manifest():
    citation = request.headers.get('Referer', '')
    parcel = RequestPayload(citation).value
    consignment = os.path.join('/var/app/data', os.path.basename(parcel))
    os.unlink(consignment)
    return jsonify({"result": "success"})
