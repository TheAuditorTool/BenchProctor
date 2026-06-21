# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest65645():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return render_template_string(data)
