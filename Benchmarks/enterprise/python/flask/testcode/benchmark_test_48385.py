# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest48385():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
