# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest54702():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
