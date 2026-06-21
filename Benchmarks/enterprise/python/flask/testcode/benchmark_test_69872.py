# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest69872():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
