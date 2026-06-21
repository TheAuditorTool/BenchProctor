# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33766():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
