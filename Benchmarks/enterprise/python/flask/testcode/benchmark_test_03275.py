# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest03275():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
