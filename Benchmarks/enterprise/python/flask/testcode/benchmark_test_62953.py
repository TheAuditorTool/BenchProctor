# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62953():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
