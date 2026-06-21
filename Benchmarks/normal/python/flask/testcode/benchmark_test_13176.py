# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest13176():
    header_value = request.headers.get('X-Custom-Header', '')
    defusedxml.ElementTree.fromstring(str(header_value))
    return jsonify({"result": "success"})
