# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest57202():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    return Markup('<div>' + str(data) + '</div>')
