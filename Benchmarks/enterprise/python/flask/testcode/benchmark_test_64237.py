# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64237():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
