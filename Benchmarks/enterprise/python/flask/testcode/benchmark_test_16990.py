# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import json


def BenchmarkTest16990():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    return Markup('<div>' + str(data) + '</div>')
