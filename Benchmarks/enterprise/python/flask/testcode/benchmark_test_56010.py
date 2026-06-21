# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56010():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
