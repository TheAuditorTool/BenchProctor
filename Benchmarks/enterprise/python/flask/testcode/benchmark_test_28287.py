# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest28287(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
