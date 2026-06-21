# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest70487():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
