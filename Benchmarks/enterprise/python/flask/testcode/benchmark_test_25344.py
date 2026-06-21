# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25344():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
