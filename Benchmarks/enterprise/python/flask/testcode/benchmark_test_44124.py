# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest44124():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    return redirect(str(data))
