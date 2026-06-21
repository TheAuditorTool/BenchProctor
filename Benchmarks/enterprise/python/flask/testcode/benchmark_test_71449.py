# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest71449():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
