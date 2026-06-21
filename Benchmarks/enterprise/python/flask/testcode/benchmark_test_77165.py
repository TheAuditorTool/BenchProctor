# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77165():
    xml_value = request.get_data(as_text=True)
    with open('output.csv', 'a') as fh:
        fh.write(str(xml_value) + ',data\n')
    return jsonify({"result": "success"})
