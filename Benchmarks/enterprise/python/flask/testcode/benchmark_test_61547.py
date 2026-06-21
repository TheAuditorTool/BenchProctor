# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest61547():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
