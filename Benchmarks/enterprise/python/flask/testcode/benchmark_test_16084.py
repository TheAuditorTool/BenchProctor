# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def BenchmarkTest16084():
    multipart_value = request.form.get('multipart_field', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(multipart_value))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
