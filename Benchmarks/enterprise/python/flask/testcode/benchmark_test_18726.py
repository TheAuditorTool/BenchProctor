# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest18726():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    return Markup('<img src="' + str(data) + '">')
