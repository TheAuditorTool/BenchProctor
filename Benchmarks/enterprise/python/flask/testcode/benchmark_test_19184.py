# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest19184():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
