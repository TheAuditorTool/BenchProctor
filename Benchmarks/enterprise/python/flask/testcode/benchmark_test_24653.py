# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def BenchmarkTest24653():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
