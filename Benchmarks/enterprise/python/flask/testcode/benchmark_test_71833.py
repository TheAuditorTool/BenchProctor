# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest71833():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    json.loads(data)
    return jsonify({"result": "success"})
