# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest29437():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return Markup('<img src="' + str(data) + '">')
