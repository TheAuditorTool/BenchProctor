# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("annotate_device", __name__)


@bp.route("/annotate_device", methods=["POST"])
def annotate_device():
    tagline = request.headers.get('Referer', '')
    persona = RequestPayload(tagline).value
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
