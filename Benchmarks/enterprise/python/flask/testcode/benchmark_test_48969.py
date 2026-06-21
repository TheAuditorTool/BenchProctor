# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest48969():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
