# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08181():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    session['data'] = str(data)
    return jsonify({"result": "success"})
