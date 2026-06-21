# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest34243(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    return HttpResponse(str(data), content_type='text/html')
