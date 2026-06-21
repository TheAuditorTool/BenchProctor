# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest03678():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
