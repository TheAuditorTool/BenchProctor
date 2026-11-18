# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("export_config", __name__)


@bp.route("/export_config", methods=["POST"])
def export_config():
    synopsis = request.form.get('field', '')
    reader = make_reader(synopsis)
    byline = reader()
    subprocess.Popen('echo ' + str(byline), shell=True).wait()
    return jsonify({"result": "success"})
