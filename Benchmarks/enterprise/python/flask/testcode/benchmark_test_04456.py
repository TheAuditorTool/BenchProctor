# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04456():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
