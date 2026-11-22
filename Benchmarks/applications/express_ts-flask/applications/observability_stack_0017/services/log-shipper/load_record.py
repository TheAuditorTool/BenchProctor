# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("load_record", __name__)


@bp.route("/load_record", methods=["POST"])
def load_record():
    note = request.headers.get('Referer', '')
    cohort = RequestPayload(note).value
    parsed = yaml.safe_load(cohort)
    return jsonify({'parsed': str(parsed)}), 200
