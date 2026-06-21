# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12235():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    int(str(data))
    return jsonify({"result": "success"})
