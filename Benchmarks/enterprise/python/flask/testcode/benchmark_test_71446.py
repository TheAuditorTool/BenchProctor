# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71446():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
