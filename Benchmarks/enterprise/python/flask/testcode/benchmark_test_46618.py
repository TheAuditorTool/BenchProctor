# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest46618():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return Markup('<div>' + str(data) + '</div>')
