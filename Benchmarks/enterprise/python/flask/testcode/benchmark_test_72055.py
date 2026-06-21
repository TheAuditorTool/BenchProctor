# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest72055():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
