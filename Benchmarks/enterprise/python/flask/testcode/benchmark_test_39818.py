# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest39818():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
