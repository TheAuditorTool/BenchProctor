# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest05837():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
