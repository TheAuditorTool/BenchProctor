# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("compact_roster", __name__)


@bp.route("/compact_roster", methods=["POST"])
def compact_roster():
    heading = request.headers.get('Referer', '')
    voucher = RequestPayload(heading).value
    backorder = os.path.join('/var/app/data', os.path.basename(voucher))
    os.unlink(backorder)
    return jsonify({"result": "success"})
