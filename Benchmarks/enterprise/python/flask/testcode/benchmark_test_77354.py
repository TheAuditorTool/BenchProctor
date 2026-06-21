# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77354():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
