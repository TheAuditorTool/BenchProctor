# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest63759():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    return Markup('<div>' + str(data) + '</div>')
