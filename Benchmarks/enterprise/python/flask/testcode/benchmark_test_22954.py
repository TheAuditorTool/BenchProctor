# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def relay_value(value):
    return value

def BenchmarkTest22954():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
