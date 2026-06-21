# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest15640():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return Markup('<img src="' + str(data) + '">')
