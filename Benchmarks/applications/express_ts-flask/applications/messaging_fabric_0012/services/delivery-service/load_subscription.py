# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("load_subscription", __name__)


@bp.route("/load_subscription", methods=["POST"])
def load_subscription():
    preface = (request.get_json(silent=True) or {}).get('payload', '')
    bulletin = preface if preface else 'default'
    os.system('echo ' + str(bulletin))
    return jsonify({"result": "success"})
