# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import json


def BenchmarkTest22926():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    return redirect(str(data))
