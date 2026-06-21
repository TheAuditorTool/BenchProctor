# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest52892():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
