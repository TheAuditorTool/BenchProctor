# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest30468():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
