# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest69878():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
