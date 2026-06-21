# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest21045():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
