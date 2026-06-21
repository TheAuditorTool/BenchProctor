# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77148():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
