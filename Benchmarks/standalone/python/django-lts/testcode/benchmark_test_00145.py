# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00145(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    resp = HttpResponse(status=302)
    resp['Location'] = str(data)
    return resp
