# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import base64
from flask import request


def BenchmarkTest41795():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
