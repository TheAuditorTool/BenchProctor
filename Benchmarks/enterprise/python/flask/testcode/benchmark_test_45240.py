# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import defusedxml.ElementTree


def BenchmarkTest45240():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
