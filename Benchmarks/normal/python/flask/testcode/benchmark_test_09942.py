# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09942():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
