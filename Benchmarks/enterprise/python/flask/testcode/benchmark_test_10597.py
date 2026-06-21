# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import runpy


def coalesce_blank(value):
    return value or ''

def BenchmarkTest10597():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
