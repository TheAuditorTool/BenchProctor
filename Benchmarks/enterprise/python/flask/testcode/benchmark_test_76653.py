# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76653():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
