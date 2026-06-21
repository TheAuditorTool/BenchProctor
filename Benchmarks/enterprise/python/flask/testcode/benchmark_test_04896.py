# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest04896():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
