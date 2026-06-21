# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest38274():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
