# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def relay_value(value):
    return value

def BenchmarkTest60742():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
