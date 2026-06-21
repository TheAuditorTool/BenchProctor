# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest27510():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
