# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12097():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
