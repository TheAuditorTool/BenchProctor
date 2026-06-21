# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest40544():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
