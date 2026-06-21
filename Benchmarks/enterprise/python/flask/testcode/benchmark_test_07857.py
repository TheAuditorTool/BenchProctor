# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def BenchmarkTest07857():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
