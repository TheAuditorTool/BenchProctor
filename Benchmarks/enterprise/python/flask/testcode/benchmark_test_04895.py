# SPDX-License-Identifier: Apache-2.0
import tempfile
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest04895():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
