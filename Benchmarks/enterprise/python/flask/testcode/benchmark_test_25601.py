# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25601():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
