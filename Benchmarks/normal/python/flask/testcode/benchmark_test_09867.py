# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest09867():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
