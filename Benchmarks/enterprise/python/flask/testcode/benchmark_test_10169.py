# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest10169():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
