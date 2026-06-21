# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest07024():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
