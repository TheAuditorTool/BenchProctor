# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import runpy
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00547():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
