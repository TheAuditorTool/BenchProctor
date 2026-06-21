# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest56664():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
