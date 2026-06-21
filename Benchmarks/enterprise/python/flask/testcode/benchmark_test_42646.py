# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess
from app_runtime import db


def BenchmarkTest42646():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    prefix = ''
    data = prefix + str(comment_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
