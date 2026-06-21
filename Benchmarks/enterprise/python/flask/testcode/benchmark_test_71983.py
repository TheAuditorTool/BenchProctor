# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest71983():
    field_value = request.form.get('field', '')
    return Markup('<div>' + str(field_value) + '</div>')
