# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest49412():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return Markup('<div>' + str(data) + '</div>')
