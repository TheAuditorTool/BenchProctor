# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06611():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
