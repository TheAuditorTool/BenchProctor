# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest23981():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    return Markup('<div>' + str(data) + '</div>')
