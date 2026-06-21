# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02144():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
