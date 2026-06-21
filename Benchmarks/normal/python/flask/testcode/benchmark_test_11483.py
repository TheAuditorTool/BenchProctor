# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest11483():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
