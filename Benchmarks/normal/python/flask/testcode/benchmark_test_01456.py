# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest01456():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    return Markup('<div>' + str(data) + '</div>')
