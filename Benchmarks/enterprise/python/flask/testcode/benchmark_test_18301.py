# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def BenchmarkTest18301():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
