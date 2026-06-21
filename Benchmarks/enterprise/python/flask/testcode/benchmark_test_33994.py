# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import runpy


def BenchmarkTest33994():
    xml_value = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', xml_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = xml_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
