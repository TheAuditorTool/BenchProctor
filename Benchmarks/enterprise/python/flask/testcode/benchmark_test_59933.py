# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59933():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
