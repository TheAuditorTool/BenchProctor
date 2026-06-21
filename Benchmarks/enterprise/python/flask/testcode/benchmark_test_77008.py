# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77008():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
