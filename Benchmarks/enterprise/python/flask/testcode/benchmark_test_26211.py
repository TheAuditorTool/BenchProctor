# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest26211():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
