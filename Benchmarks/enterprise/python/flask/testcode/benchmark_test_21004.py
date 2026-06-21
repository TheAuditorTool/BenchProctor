# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import json


def BenchmarkTest21004():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
