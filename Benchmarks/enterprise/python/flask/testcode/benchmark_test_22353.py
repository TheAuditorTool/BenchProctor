# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest22353():
    auth_header = request.headers.get('Authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
