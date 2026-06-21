# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42833():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
