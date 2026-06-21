# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest60234():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    return Markup('<div>' + str(data) + '</div>')
