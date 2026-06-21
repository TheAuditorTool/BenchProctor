# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest13473(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return HttpResponse('<html><body><h1>' + str(origin_value) + '</h1></body></html>', content_type='text/html')
