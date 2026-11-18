# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("compact_bundle", __name__)


@bp.route("/compact_bundle", methods=["POST"])
def compact_bundle():
    snippet = request.headers.get('Referer', '')
    persona = RequestPayload(snippet).value
    handshake = os.path.join('/var/app/data', os.path.basename(persona))
    os.unlink(handshake)
    return jsonify({"result": "success"})
