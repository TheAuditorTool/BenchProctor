# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest52185():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return str(data), 200, {'Content-Type': 'text/html'}
