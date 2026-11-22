# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("audit_schedule", __name__)


@bp.route("/audit_schedule", methods=["POST"])
def audit_schedule():
    snippet = request.headers.get('Referer', '')
    inquiry = RequestPayload(snippet).value
    parsed = yaml.safe_load(inquiry)
    return jsonify({'parsed': str(parsed)}), 200
