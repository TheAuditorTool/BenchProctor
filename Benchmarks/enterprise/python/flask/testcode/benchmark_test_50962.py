# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest50962():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
