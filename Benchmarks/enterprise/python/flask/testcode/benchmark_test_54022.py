# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest54022():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
