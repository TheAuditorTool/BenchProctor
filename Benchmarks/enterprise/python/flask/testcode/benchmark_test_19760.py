# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest19760(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
