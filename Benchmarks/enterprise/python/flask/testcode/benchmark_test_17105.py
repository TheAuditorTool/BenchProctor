# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest17105():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return Markup('<div>' + str(data) + '</div>')
