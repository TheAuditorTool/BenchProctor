# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest35233():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
