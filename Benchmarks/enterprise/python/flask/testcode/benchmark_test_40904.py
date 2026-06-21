# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40904():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
