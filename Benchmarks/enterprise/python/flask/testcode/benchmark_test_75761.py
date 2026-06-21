# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest75761():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return Markup('<img src="' + str(data) + '">')
