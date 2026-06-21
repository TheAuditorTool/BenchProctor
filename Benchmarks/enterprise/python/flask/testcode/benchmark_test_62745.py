# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest62745():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
