# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest57761():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
