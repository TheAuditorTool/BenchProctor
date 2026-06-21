# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12745():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
