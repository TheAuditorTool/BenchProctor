# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest03856():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
