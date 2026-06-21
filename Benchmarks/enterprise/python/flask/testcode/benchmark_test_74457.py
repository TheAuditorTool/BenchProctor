# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess
from app_runtime import db


def BenchmarkTest74457():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = comment_value
            data = parsed
        case _:
            data = comment_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
