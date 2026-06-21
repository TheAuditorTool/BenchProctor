# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest33855():
    ua_value = request.headers.get('User-Agent', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(ua_value))
    return redirect(target)
