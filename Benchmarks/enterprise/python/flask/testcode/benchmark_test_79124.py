# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest79124():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
