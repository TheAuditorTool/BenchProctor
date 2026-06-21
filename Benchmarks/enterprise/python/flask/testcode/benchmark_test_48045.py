# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest48045():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    return Markup('<div>' + str(data) + '</div>')
