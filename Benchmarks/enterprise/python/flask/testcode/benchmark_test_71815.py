# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71815():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    yaml.safe_load(data)
    return jsonify({"result": "success"})
