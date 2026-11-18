# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("resolve_snapshot", __name__)


@bp.route("/resolve_snapshot", methods=["POST"])
def resolve_snapshot():
    remark = request.form.get('field', '')
    remittance = f'{remark!s}'
    s = socket.create_connection((str(remittance), 80))
    s.close()
    return jsonify({"result": "success"})
