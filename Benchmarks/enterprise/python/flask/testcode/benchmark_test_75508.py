# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest75508():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
