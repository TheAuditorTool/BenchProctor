# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12824():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
