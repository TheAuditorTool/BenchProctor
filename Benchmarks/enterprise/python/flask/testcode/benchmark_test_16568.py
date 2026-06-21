# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest16568():
    referer_value = request.headers.get('Referer', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(referer_value))
    return redirect(target)
