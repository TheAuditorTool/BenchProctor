# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def BenchmarkTest49019():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
