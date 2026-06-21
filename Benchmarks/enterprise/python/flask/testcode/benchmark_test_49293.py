# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest49293():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
