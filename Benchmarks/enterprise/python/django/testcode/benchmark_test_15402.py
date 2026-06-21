# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest15402(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    return HttpResponse(str(data), content_type='text/html')
