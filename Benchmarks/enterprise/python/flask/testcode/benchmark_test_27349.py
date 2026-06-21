# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest27349():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
