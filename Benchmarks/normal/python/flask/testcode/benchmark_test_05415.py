# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05415():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
