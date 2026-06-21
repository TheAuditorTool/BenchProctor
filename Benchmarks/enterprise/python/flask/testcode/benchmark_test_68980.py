# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest68980():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
