# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest07428():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
