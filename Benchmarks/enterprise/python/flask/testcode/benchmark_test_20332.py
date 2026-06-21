# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20332():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
