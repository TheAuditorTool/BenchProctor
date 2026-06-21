# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest04978():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return Markup('<div>' + str(data) + '</div>')
