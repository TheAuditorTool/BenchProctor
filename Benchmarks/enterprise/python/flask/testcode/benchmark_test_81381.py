# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest81381():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
