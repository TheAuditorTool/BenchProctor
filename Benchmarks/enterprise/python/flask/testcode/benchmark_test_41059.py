# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest41059():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
