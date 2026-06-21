# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
from flask import request


def BenchmarkTest57322():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
