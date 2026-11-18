# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("compact_flag", __name__)


@bp.route("/compact_flag", methods=["POST"])
def compact_flag():
    passage = request.files['upload'].filename
    reader = make_reader(passage)
    persona = reader()
    yaml.load(persona, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
