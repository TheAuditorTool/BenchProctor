# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest66149():
    referer_value = request.headers.get('Referer', '')
    processed = html.escape(referer_value)
    return Markup('<div>' + str(processed) + '</div>')
