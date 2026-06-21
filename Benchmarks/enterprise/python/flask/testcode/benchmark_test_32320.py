# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest32320():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
