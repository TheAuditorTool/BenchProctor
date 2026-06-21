# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest26126():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
