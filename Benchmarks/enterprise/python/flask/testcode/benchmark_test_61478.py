# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest61478():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
