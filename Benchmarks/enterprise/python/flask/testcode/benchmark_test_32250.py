# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest32250():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    return redirect(str(data))
