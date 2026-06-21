# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest07343():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    return Markup('<img src="' + str(data) + '">')
