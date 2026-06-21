# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest56158():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
