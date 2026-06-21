# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest22368():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    return Markup('<img src="' + str(data) + '">')
