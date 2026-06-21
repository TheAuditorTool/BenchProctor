# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import request, jsonify
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest45431():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
