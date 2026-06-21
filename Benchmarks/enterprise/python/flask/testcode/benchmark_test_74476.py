# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata
from types import SimpleNamespace


def BenchmarkTest74476():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
