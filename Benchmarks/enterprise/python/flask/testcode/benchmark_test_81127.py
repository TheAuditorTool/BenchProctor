# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest81127():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    int(str(data))
    return jsonify({"result": "success"})
