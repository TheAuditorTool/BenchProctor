# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest24668():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
