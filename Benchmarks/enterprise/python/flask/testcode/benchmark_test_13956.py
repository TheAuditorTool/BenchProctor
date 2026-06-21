# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import json


def BenchmarkTest13956():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
