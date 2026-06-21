# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest68387():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
