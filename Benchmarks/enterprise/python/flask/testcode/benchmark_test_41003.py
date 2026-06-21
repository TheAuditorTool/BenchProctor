# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import json
import urllib.parse


def BenchmarkTest41003():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
