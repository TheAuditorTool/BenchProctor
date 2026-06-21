# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest80306():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    return redirect(str(data))
