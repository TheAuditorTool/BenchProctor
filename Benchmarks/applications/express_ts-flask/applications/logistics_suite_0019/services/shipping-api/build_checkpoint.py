# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("build_checkpoint", __name__)


@bp.route("/build_checkpoint", methods=["POST"])
def build_checkpoint():
    citation = request.headers.get('Referer', '')
    parcel = RequestPayload(citation).value
    parsed = yaml.safe_load(parcel)
    return jsonify({'parsed': str(parsed)}), 200
