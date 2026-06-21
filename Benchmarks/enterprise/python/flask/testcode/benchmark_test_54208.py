# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54208():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
