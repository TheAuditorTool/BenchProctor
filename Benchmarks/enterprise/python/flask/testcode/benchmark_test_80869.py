# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80869():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
