# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


def BenchmarkTest16235():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
