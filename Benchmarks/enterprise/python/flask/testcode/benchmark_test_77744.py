# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest77744():
    upload_name = request.files['upload'].filename
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(upload_name))
    return jsonify({"result": "success"})
