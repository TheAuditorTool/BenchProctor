# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest04237():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
