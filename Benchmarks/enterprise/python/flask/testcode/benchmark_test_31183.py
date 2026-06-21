# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31183():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
