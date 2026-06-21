# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest04994():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return Markup('<div>' + str(data) + '</div>')
