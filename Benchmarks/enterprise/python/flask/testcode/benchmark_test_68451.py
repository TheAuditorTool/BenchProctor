# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest68451():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
