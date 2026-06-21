# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79926():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    session['data'] = str(data)
    return jsonify({"result": "success"})
