# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest06681():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
