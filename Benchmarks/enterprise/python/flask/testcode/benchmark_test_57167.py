# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest57167():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
