# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest52460():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
