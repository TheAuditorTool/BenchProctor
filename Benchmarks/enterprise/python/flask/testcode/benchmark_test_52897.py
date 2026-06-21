# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest52897():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return Markup('<img src="' + str(data) + '">')
