# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest23732():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
