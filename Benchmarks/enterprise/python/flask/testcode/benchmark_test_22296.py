# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest22296():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    return redirect(str(data))
