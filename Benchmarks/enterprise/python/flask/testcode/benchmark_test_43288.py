# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest43288():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
