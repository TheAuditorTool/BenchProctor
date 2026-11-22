# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("fetch_record", __name__)


@bp.route("/fetch_record", methods=["POST"])
def fetch_record():
    snippet = request.headers.get('Referer', '')
    addendum = RequestPayload(snippet).value
    parsed = yaml.safe_load(addendum)
    return jsonify({'parsed': str(parsed)}), 200
