# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("validate_summary", __name__)


@bp.route("/validate_summary", methods=["POST"])
def validate_summary():
    caption = request.headers.get('Referer', '')
    remittance = RequestPayload(caption).value
    parsed = yaml.safe_load(remittance)
    return jsonify({'parsed': str(parsed)}), 200
