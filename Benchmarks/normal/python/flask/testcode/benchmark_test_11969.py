# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11969():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
