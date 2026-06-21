# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest45107():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return Markup('<div>' + str(data) + '</div>')
