# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest60573():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    return redirect(str(data))
