# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48249():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
