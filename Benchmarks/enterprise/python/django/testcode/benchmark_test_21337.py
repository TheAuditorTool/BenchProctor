# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest21337(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return HttpResponse(str(data), content_type='text/html')
