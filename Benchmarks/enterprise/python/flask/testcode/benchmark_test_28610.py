# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest28610():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
