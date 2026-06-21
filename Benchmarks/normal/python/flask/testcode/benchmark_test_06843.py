# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import runpy
from app_runtime import db


def BenchmarkTest06843():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(comment_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
