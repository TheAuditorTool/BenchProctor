# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49932():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    int(str(data))
    return jsonify({"result": "success"})
