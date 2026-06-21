# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def BenchmarkTest12789():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
