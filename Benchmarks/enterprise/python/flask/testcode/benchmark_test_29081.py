# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest29081():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
