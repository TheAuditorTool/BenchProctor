# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76811():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
