# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest03867():
    xml_value = request.get_data(as_text=True)
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return Markup('<div>' + str(data) + '</div>')
