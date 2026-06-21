# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15050():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
