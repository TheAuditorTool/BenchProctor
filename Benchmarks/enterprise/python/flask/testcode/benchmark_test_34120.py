# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest34120():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return redirect(str(data))
