# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest40227():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
