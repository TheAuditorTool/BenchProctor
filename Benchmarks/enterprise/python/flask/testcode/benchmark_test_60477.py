# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest60477():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
