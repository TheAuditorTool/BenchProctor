# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00680(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    return redirect(str(data))
