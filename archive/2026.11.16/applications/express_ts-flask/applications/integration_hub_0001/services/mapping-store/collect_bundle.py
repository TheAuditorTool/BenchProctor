# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("collect_bundle", __name__)


@bp.route("/collect_bundle", methods=["POST"])
def collect_bundle():
    quotation = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(quotation)
    handshake = reader()
    pickle.loads(base64.b64decode(handshake))
    return jsonify({"result": "success"})
