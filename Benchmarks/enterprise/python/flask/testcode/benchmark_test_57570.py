# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest57570():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return redirect(str(data))
