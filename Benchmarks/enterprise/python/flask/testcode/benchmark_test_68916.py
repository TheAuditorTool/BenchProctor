# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest68916():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
