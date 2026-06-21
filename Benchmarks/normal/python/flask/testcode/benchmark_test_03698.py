# SPDX-License-Identifier: Apache-2.0
import tempfile
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest03698():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
