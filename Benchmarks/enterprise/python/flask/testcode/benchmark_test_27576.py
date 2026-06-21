# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
import json


def BenchmarkTest27576():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
