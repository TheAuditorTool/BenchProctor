# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import request, jsonify
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest47235():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
