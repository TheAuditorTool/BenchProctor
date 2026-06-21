# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80671(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
