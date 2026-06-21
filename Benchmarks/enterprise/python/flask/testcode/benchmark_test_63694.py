# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import runpy
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest63694():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
