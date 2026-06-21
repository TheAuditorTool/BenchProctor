# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest19381():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
