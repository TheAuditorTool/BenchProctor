# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71431():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
