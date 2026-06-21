# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47103():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
