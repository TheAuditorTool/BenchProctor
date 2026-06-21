# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest24472():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return Markup('<div>' + str(data) + '</div>')
