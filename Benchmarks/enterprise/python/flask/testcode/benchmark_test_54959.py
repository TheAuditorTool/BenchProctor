# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54959():
    upload_name = request.files['upload'].filename
    match str(upload_name):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
