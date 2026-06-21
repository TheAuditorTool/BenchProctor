# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55172():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
