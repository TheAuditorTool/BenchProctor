# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest18601():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    requests.get(str(data))
    return jsonify({"result": "success"})
