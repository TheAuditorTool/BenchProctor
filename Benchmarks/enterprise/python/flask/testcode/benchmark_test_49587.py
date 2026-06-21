# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest49587():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
