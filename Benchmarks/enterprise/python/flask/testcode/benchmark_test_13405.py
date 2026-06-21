# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13405():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
