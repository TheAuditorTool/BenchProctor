# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest64208():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
