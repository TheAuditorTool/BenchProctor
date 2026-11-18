# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("render_ticket", __name__)


@bp.route("/render_ticket", methods=["POST"])
def render_ticket():
    phrase = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(phrase)
    subprocess.run('echo ' + str(inquiry), shell=True)
    return jsonify({"result": "success"})
