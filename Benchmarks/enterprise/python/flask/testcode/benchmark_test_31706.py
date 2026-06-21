# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote
from flask import request


def BenchmarkTest31706():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
