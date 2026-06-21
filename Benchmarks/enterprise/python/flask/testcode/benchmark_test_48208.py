# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest48208():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
