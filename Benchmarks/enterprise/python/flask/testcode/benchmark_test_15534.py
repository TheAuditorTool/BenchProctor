# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest15534(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
