# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest24304():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
