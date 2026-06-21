# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest25793():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    return redirect(str(data))
