# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest22489():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
