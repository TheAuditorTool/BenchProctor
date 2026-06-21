# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import request, jsonify
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest17000():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
