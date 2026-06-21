# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24061():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
