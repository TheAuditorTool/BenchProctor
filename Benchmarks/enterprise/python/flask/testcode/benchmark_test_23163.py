# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import json
import urllib.parse


def BenchmarkTest23163():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
