# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25999():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
