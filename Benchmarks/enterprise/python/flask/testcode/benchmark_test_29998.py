# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest29998():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
