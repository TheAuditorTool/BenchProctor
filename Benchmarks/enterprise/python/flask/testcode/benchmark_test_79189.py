# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest79189():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
