# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest01052():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return redirect(str(data))
