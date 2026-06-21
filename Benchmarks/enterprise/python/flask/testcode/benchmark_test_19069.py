# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest19069():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return redirect(str(data))
