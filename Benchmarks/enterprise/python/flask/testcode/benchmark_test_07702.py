# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest07702():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    subprocess.run('echo ' + str(comment_value), shell=True)
    return jsonify({"result": "success"})
