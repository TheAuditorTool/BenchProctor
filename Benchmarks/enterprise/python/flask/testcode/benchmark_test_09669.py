# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09669(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
