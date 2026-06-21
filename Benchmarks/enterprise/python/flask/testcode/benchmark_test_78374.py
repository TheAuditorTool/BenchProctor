# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest78374():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
