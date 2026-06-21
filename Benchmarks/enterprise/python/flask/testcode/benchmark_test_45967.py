# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45967():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
