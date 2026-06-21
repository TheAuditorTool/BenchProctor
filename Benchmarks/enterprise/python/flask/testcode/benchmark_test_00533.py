# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request
import json


def BenchmarkTest00533():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
