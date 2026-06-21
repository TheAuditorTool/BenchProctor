# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest03251():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    return Markup('<div>' + str(data) + '</div>')
