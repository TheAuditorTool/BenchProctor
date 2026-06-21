# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import runpy


def BenchmarkTest48509():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
