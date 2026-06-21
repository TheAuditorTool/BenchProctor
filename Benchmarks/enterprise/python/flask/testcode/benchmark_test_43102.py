# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
import unicodedata


def BenchmarkTest43102():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
