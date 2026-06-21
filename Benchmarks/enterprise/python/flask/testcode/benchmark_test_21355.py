# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest21355():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
