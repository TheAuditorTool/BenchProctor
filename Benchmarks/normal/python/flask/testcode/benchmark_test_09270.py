# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest09270():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return redirect(str(data))
