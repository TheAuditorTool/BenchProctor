# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import runpy
from app_runtime import db


def BenchmarkTest51254():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
