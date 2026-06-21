# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest69892():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
