# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest11925():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
