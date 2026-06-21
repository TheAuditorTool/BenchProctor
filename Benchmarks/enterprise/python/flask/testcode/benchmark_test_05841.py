# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest05841():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
