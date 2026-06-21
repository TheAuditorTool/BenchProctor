# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02626():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
