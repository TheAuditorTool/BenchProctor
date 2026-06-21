# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest05385(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
