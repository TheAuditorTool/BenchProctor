# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest16549():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
