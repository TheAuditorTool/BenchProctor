# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("load_record", __name__)


@bp.route("/load_record", methods=["POST"])
def load_record():
    excerpt = request.args.get('id', '')
    reader = make_reader(excerpt)
    restock = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(restock) + "'")
    return jsonify({"result": "success"})
