# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest72448():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
