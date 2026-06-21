# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest31765():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
