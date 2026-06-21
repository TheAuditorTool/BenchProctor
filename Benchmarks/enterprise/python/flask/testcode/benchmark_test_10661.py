# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata
from types import SimpleNamespace


def BenchmarkTest10661():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
