# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01998():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
