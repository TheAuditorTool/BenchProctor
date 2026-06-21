# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25872():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
