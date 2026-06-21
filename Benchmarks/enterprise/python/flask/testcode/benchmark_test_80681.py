# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def BenchmarkTest80681():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
