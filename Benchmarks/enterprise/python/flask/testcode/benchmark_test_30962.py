# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30962():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
