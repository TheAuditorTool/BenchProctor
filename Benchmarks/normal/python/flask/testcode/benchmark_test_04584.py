# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04584():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
