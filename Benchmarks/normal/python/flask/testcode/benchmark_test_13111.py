# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13111():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    session['user'] = str(data)
    return jsonify({"result": "success"})
