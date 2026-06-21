# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04720():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
