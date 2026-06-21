# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import json
import urllib.parse


def BenchmarkTest66775():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
