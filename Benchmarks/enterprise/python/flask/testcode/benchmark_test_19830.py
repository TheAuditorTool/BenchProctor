# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest19830():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
