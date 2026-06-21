# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest09653():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
