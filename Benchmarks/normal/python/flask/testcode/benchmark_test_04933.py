# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest04933():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return Markup('<div>' + str(data) + '</div>')
