# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_window", __name__)


@bp.route("/resolve_window", methods=["POST"])
def resolve_window():
    notice = request.args.get('id', '')
    reader = make_reader(notice)
    backorder = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(backorder) + "'")
    return jsonify({"result": "success"})
