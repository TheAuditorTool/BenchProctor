# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import pickle


def relay_value(value):
    return value

def BenchmarkTest79480():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})
