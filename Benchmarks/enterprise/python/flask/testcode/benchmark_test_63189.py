# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63189():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
