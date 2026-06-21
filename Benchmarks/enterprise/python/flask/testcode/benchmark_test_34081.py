# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34081():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
