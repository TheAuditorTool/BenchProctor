# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest11733():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
