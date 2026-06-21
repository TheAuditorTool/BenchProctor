# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48943():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    json.loads(data)
    return jsonify({"result": "success"})
