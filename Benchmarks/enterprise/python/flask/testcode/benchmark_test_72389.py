# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest72389():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
