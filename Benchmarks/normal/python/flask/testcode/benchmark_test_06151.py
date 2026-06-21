# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06151():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
