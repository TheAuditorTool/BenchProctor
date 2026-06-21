# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest81174():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return Markup('<div>' + str(data) + '</div>')
