# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest63090():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
