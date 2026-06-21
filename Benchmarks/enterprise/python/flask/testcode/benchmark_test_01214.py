# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01214():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
