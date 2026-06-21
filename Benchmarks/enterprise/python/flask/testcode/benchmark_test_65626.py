# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest65626():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
