# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01013():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
