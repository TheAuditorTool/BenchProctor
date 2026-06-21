# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest73273():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
