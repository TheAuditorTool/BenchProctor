# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def BenchmarkTest10188():
    xml_value = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', xml_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = xml_value
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
