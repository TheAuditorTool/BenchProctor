# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponseRedirect


def BenchmarkTest00145(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    return HttpResponseRedirect(str(data))
