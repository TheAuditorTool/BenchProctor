# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest18846():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
