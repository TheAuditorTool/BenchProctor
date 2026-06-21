# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest11147():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return Markup('<div>' + str(data) + '</div>')
