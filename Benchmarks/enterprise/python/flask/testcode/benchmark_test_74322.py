# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def normalise_input(value):
    return value.strip()

def BenchmarkTest74322():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
