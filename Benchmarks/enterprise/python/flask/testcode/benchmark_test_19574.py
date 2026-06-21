# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest19574():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
