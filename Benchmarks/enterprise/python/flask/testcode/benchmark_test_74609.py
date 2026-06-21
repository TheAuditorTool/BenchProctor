# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest74609():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    return redirect(str(data))
