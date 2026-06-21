# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26810():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    yaml.safe_load(data)
    return jsonify({"result": "success"})
