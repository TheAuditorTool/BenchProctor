# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09971():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
