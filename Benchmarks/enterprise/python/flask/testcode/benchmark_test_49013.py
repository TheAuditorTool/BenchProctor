# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace
import tempfile
from app_runtime import db


def BenchmarkTest49013():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return jsonify({"result": "success"})
