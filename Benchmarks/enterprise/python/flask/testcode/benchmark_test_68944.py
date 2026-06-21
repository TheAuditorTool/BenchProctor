# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def relay_value(value):
    return value

def BenchmarkTest68944():
    header_value = request.headers.get('X-Custom-Header', '')
    data = relay_value(header_value)
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
