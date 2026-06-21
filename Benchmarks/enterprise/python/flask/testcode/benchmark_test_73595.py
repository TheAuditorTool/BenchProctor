# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73595():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
