# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest02126():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return redirect(str(data))
