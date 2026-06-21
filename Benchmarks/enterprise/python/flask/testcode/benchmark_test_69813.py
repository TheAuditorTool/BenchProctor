# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import json


def BenchmarkTest69813():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    return Markup('<div>' + str(data) + '</div>')
