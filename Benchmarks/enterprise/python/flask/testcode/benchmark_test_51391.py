# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest51391():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return Markup('<div>' + str(data) + '</div>')
