# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("build_manifest", __name__)


@bp.route("/build_manifest", methods=["POST"])
def build_manifest():
    preface = request.get_data(as_text=True)
    reader = make_reader(preface)
    addendum = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", addendum):
        return jsonify({'error': 'forbidden'}), 400
    dossier = addendum
    subprocess.Popen('echo ' + str(dossier), shell=True).wait()
    return jsonify({"result": "success"})
