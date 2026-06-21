# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest70368():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    json.loads(data)
    return jsonify({"result": "success"})
