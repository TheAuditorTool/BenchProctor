# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest00656():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
