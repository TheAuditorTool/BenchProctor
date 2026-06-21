# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest60612():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
