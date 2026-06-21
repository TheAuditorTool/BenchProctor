# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest04018():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
