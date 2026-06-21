# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest20227():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
