# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import json


def BenchmarkTest63180():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    return render_template_string(data)
