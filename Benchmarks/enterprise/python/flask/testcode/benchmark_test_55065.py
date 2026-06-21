# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55065():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
