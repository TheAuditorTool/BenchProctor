# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08137():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<img src="' + str(processed) + '">')
