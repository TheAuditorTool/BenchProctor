# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40834():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
