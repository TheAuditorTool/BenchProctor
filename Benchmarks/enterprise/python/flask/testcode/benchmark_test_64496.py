# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest64496():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
