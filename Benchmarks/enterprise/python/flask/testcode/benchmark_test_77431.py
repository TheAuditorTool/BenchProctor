# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77431():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
