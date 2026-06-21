# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59272():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
