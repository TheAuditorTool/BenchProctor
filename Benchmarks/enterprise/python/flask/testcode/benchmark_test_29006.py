# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest29006():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    return Markup('<div>' + str(data) + '</div>')
