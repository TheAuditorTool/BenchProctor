# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("prune_digest", __name__)


@bp.route("/prune_digest", methods=["POST"])
def prune_digest():
    notice = request.form.get('field', '')
    reader = make_reader(notice)
    persona = reader()
    subprocess.Popen('echo ' + str(persona), shell=True).wait()
    return jsonify({"result": "success"})
