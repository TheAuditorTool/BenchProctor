# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest02918():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
