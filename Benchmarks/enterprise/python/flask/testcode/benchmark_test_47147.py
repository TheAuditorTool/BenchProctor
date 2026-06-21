# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47147():
    host_value = request.headers.get('Host', '')
    data = default_blank(host_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
