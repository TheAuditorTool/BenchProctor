# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest59313():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
