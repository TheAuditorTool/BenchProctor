# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest02582():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    return redirect(str(data))
