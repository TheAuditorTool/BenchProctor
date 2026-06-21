# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest12549():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
