# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66711():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
