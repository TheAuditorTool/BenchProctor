# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def to_text(value):
    return str(value).strip()

def BenchmarkTest64790():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
