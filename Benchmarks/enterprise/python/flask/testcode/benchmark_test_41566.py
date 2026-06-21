# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest41566():
    multipart_value = request.form.get('multipart_field', '')
    processed = html.escape(multipart_value)
    return Markup('<img src="' + str(processed) + '">')
