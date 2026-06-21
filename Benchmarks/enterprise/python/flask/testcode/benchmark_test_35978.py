# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35978():
    raw_body = request.get_data(as_text=True)
    eval(str(raw_body))
    return jsonify({"result": "success"})
