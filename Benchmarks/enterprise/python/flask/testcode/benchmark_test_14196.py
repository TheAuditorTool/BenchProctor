# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest14196():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
