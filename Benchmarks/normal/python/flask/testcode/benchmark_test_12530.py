# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest12530():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
