# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import json
import urllib.parse


def BenchmarkTest28465():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
