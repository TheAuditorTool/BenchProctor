# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest59060():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
