# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09149():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
