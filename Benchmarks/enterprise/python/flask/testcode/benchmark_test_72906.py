# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72906():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
