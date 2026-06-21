# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import tempfile
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest32958():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
