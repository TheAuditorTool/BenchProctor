# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest53198():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
