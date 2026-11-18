# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_supplier", __name__)


@bp.route("/audit_supplier", methods=["POST"])
def audit_supplier():
    summary = request.files['upload'].filename
    reader = make_reader(summary)
    restock = reader()
    yaml.load(restock, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
