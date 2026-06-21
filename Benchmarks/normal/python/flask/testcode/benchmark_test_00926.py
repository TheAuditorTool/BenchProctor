# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00926():
    xml_value = request.get_data(as_text=True)
    try:
        os.setuid(int(str(xml_value)) if str(xml_value).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
