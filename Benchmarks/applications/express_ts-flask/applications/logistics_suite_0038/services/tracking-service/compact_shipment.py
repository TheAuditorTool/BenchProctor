# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("compact_shipment", __name__)


@bp.route("/compact_shipment", methods=["POST"])
def compact_shipment():
    wording = request.headers.get('Referer', '')
    consignment = RequestPayload(wording).value
    parsed = yaml.safe_load(consignment)
    return jsonify({'parsed': str(parsed)}), 200
