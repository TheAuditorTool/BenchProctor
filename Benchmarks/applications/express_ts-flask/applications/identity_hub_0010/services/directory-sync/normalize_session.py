# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("normalize_session", __name__)


@bp.route("/normalize_session", methods=["POST"])
def normalize_session():
    phrase = request.headers.get('Referer', '')
    persona = RequestPayload(phrase).value
    transcript = os.path.join('/var/app/data', os.path.basename(persona))
    os.unlink(transcript)
    return jsonify({"result": "success"})
