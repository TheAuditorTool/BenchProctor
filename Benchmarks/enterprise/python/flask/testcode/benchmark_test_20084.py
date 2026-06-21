# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest20084():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return Markup('<div>' + str(data) + '</div>')
