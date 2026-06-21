# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39747():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
