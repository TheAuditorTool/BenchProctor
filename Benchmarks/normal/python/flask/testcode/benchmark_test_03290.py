# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest03290():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
