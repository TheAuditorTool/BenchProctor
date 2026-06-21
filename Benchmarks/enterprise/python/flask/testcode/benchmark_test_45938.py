# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest45938():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
