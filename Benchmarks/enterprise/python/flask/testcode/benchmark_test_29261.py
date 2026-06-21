# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest29261():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
