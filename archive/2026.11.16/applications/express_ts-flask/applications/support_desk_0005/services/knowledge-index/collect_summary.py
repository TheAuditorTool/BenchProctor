# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("collect_summary", __name__)


@bp.route("/collect_summary", methods=["POST"])
def collect_summary():
    phrase = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(phrase)
    inquiry = reader()
    pickle.loads(base64.b64decode(inquiry))
    return jsonify({"result": "success"})
