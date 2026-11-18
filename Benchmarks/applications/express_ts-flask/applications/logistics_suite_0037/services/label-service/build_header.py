# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("build_header", __name__)


@bp.route("/build_header", methods=["POST"])
def build_header():
    footnote = request.headers.get('Referer', '')
    consignment = RequestPayload(footnote).value
    parcel = os.path.join('/var/app/data', os.path.basename(consignment))
    os.unlink(parcel)
    return jsonify({"result": "success"})
