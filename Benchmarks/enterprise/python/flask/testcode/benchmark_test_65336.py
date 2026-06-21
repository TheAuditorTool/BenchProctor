# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest65336():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
