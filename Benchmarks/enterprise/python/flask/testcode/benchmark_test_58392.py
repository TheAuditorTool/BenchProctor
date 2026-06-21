# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58392():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
