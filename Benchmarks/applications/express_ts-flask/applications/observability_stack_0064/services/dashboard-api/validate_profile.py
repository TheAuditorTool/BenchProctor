# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("validate_profile", __name__)


@bp.route("/validate_profile", methods=["POST"])
def validate_profile():
    tagline = request.args.get('id', '')
    reader = make_reader(tagline)
    gauge = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return jsonify({"result": "success"})
