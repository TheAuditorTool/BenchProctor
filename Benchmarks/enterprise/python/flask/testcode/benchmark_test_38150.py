# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest38150():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
