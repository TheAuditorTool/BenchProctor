# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("verify_profile", __name__)


@bp.route("/verify_profile", methods=["POST"])
def verify_profile():
    synopsis = request.headers.get('Referer', '')
    verdict = RequestPayload(synopsis).value
    grievance = os.path.join('/var/app/data', os.path.basename(verdict))
    os.unlink(grievance)
    return jsonify({"result": "success"})
