# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest20471():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
