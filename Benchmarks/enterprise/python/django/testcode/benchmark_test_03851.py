# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest03851(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    return HttpResponse(str(data), content_type='text/html')
