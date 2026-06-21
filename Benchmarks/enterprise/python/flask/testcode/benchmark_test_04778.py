# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote
from flask import request


def BenchmarkTest04778():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
