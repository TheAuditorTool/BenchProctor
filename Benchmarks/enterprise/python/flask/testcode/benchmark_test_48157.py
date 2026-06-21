# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest48157():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
