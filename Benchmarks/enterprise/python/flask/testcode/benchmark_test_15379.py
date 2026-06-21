# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15379():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
