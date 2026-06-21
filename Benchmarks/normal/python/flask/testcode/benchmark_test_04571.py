# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest04571():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    defusedxml.ElementTree.fromstring(str(json_value))
    return jsonify({"result": "success"})
