# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25181():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
