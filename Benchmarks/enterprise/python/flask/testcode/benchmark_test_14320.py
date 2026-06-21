# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14320():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
