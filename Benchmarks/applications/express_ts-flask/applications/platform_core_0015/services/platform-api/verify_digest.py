# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("verify_digest", __name__)


@bp.route("/verify_digest", methods=["POST"])
def verify_digest():
    note = request.files['upload'].filename
    reader = make_reader(note)
    handshake = reader()
    yaml.load(handshake, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
