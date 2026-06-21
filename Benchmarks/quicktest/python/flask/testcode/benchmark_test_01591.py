# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest01591():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    return Markup('<div>' + str(data) + '</div>')
