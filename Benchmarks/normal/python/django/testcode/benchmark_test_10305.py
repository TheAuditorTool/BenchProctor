# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest10305(request):
    raw_body = request.body.decode('utf-8')
    with open('/var/app/data/' + str(raw_body), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
