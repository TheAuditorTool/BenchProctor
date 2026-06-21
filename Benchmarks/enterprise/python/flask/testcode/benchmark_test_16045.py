# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest16045():
    host_value = request.headers.get('Host', '')
    processed = html.escape(host_value)
    return Markup('<div>' + str(processed) + '</div>')
