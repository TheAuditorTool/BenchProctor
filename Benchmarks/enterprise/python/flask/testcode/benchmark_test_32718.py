# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest32718():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
