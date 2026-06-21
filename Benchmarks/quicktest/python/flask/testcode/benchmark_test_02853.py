# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest02853():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
