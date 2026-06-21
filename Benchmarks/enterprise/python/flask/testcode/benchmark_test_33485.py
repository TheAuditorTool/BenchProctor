# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest33485():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
