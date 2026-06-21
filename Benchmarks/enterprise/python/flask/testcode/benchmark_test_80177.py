# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest80177():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
