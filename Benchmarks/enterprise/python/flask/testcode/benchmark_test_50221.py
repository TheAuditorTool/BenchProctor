# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest50221():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
