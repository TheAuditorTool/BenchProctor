# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00979():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    os.seteuid(65534)
    return jsonify({"result": "success"})
