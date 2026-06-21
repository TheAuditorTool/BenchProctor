# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest55264():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
