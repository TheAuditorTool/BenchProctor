# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("summarize_allocation", __name__)


@bp.route("/summarize_allocation", methods=["POST"])
def summarize_allocation():
    summary = request.form.get('field', '')
    reader = make_reader(summary)
    restock = reader()
    subprocess.Popen('echo ' + str(restock), shell=True).wait()
    return jsonify({"result": "success"})
