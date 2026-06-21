# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest23250():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return Markup('<img src="' + str(data) + '">')
