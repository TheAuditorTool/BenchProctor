# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77412(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    json.loads(data)
    return jsonify({"result": "success"})
