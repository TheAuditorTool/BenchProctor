# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import defusedxml.ElementTree


def BenchmarkTest22222():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
