# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest74104():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
