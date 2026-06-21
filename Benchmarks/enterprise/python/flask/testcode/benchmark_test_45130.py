# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest45130():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
