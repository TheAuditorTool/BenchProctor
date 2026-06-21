# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def relay_value(value):
    return value

def BenchmarkTest16870():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
