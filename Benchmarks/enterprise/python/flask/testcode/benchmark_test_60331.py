# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest60331():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
