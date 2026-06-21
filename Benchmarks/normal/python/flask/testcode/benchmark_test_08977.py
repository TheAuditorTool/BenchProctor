# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08977():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
